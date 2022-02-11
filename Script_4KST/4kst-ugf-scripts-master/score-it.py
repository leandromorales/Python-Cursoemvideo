from neuromancer.utils_4kst import clear, COD_ERROS, COD_PRESTADORES
from neuromancer.api import Authenticator, download_arquivo, score_file_model, watcher_request
from time import sleep
import argparse
import pandas as pd
import os


import logging
logging.basicConfig(filename='log.csv',level=logging.INFO, format='%(levelname)s|%(name)s|%(asctime)s|%(message)s', datefmt='%Y-%m-%d %I:%M:%S')
"""
Log Configuration
"""
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s\t%(name)s\t%(asctime)s\t%(message)s')
console.setFormatter(formatter)
logging.getLogger().addHandler(console)

logger = logging.getLogger("score-it.py")
logger.setLevel(logging.INFO)

def check_guia(num_guia, df): 
    check = df['STATUS_ITEM'].loc[df['NUM_GUIA'] == num_guia].tolist()
    return "GLOSADO" if "GLOSADO" in check else "INTEGRADO"

if __name__ == '__main__':
    clear()
    parser = argparse.ArgumentParser(description='4KST UGF Glosa Score')
    parser.add_argument('path', metavar='File', type=str, help='path to csv file')
    args = parser.parse_args()
    path = args.path

    ######################
    # Carregando arquivo #
    ######################
    flag_excel = False
    try:
        if path.endswith(".xlsx") or path.endswith(".xls"):
            logger.info('Carregando arquivo {}.'.format(path))
            df = pd.read_excel(path)
            flag_excel = True
        elif path.endswith(".csv"):
            logger.info('Carregando arquivo {}.'.format(path))
            df = pd.read_csv(path, sep=';', encoding='latin1')
        else:
            raise Exception(f"File [{path}] format not supported!")
    except (NameError, Exception) as e:
        logger.error(f"Não foi possível processar o arquivo [{path}]. Razão: {e}")
        raise e
    logger.info(f'Arquivo carregado. Linhas: {df.shape[0]} Colunas: {df.shape[1]}.')

    #########################
    # Realizando Login 4KST #
    #########################
    logger.info("Autenticando acesso")
    auth = Authenticator()

    #####################
    # Normalização 4KST #
    #####################
    logger.info("Normalizando o arquivo.")
    try:
        df.rename(columns={'GUITE_NRO_SEQ':'NRO_SEQ','STATUS_ERRO_ITEM':'STATUS_ERRO','DESC_ERRO_ITEM':'DESC_ERRO',\
            'DESC_ITEM':'ITEM_DES_PRINC', 'COD_ERRO_ITEM': 'COD_ERRO','GUIA_NRO_COMPET': 'SAFRAPROP', 'COD_ID_GUIA': 'ID_GUIA',\
                'CODIGO_BENEFICIARIO': 'NRO_BNFRIO','GUIA_COD_PREST': 'COD_PREST_CAPA'}, inplace=True)
    except (NameError, Exception) as e:
        logger.error(f"Nao foi possível processar o arquivo. As colunas do arquivo não condizem com o acordado. Reason: {e}")
        del df
        raise e
    
    #####################
    # Filtrando códigos #
    #####################
    logger.info("Filtrando códigos que não devem ser processados.")
    df = df.loc[df['COD_ERRO'].isin(COD_ERROS)]
    df['COD_PREST_CAPA'] = df['COD_PREST_CAPA'].astype(int)
    df = df.loc[df['COD_PREST_CAPA'].isin(COD_PRESTADORES)]
    logger.info(f"Arquivo pós filtros: Linhas: {df.shape[0]} - Colunas: {df.shape[1]}")
    if len(df) == 0:
        logger.warn("Nenhuma linha a ser processada. Os filtros aplicados removeram todas as linhas.")
        del df
        exit()

    #####################
    # Pré processamento #
    #####################
    df_original = df.copy()
    logger.info("Pré-processando o arquivo.")
    df['4KSTGUIACOUNT'] = df.groupby('NUM_GUIA')['NUM_GUIA'].transform('count')
    df['4KSTGUIAITEMCODCOUNT'] = df.groupby(['NUM_GUIA','ITEM_COD'])['ITEM_COD'].transform('count')
    df['4KSTCODPRESTCAPAITEMCODCOUNT'] = df.groupby(['COD_PREST_CAPA','ITEM_COD'])['ITEM_COD'].transform('count')
    
    df = df.reset_index().drop(['index'], axis=1)

    logger.info("Checando nome das colunas.")
    rename_columns = {}
    for c in df.columns.values:
        rename_columns[c] = c.upper().replace("_", "")
    df.rename(columns=rename_columns, inplace=True)
    
    ###############################
    # Iniciando Upload de arquivo #
    ###############################
    logger.info("Enviando o arquivo para a 4KST.")
    watcher_id = score_file_model(auth.get(), df.copy())
    logger.info(f"Código de rastreio do processo: {watcher_id}")

    ##################################
    # Iniciando Escoragem de arquivo #
    ##################################
    status = 100
    logger.info("Iniciando escoragem.")
    while status != 200:
        status =  watcher_request(auth.get(), watcher_id)
        if status == 300:
            logger.error(f"A escoragem falhou. Código do processo: {watcher_id}")
            exit()
        sleep(5)
    logger.info("Escoragem realizada com sucesso.")

    logger.info("Baixando scores da 4KST.")
    df_scores = download_arquivo(auth.get(), watcher_id, scorename='4KST_ITEM_SCORE')

    #####################################
    # Concatenando com arquivo original #
    #####################################
    logger.info("Concatenando informações.")
    df_original = df_original.reset_index().drop(['index'], axis=1).reset_index().rename(columns={'index': 'id'})
    df_original['id'] = df_original['id'].astype(str)
    try:
        df_original = pd.merge(left=df_original, right=df_scores, left_on=['id'], right_on=['id'], how='left')
    except (NameError, Exception) as e:
        logger.error("Não foi possível concatenar o arquivo origem com os escores do modelo. Razão: {}".format(e))
        raise e
    
    logger.info("Definindo score de Guia.")
    df_guia_min_p1 = df_original.groupby(df_original.NUM_GUIA, sort = False)['4KST_ITEM_SCORE'].min()
    df_original = df_original.join(df_guia_min_p1, on='NUM_GUIA', how = 'outer', rsuffix = '_MIN')
    df_original.rename(columns={"4KST_ITEM_SCORE_MIN": "4KST_GUIA_SCORE"}, inplace=True)
    
    logger.info("Definindo o status da Guia.")
    df_original['STATUS_ITEM_GUIA'] = df_original['NUM_GUIA'].apply(lambda x: check_guia(x, df_original))

    df_original.rename(columns={'NRO_SEQ':'GUITE_NRO_SEQ','STATUS_ERRO':'STATUS_ERRO_ITEM','DESC_ERRO':'DESC_ERRO_ITEM',\
        'ITEM_DES_PRINC':'DESC_ITEM','COD_ERRO':'COD_ERRO_ITEM','SAFRAPROP':'GUIA_NRO_COMPET','ID_GUIA':'COD_ID_GUIA',\
        'NRO_BNFRIO':'CODIGO_BENEFICIARIO','COD_PREST_CAPA':'GUIA_COD_PREST'}, inplace=True)

    ####################
    # Salvando arquivo #
    ####################
    logger.info("Salvando o arquivo processado.")
    if flag_excel:
        filename = path[:-5]
        df_original.drop(['id'], axis=1).to_excel(f'{filename}_4KSTd.xlsx', engine='xlsxwriter', index=False)
        filename = f'{filename}_4KSTd.xlsx'
    else:
        filename = path[:-4]
        df_original.drop(['id'], axis=1).to_csv(f'{filename}_4KSTd.csv', index=False, sep=';', encoding='utf-8')
        filename = f'{filename}_4KSTd.csv'
    logger.info(f"Arquivo [{path}] processado com sucesso. Resultado: [{filename}].")
    ### LIBERANDO MEMORIA
    del df
    del df_scores
    del df_original
    os.remove('.tempfile')
    exit()
