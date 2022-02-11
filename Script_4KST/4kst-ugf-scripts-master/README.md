# Deploy 4KST - UGF Glosa

Esse repositório contém os scripts necessários para realizar a consulta do **4KST UGF Glosa**.

Quais são as dependências necessárias para a consulta?
 Algumas bibliotecas foram utilizadas para o desenvolvimento desse script, dentre elas é possível elencar:
- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)
- [Requests](https://requests.readthedocs.io/en/master/)

Para fazer a instalação dessas dependências é necessário instação do [Anaconda](https://www.anaconda.com/), reiniciar o terminal e utilizar dos seguintes comando:
```
conda create -y -n ugf-glosa python=3.7
conda activate ugf-glosa
conda install -y -c conda-forge -c anaconda requests pandas numpy
```


## Como realizar consultas?

Antes de mais nada, é importante que as variáveis `KEY_ID` e `KEY_SECRET` dentro do arquivo `neuromancer/api.py` estejam preenchidas com as credenciais de acesso. Se essas informações não estiverem preenchidas, **não será possível fazer conexão** com a API da 4KST.


Para utilizar é necessário executar o `score-it.py` e passar como parâmetro o caminho para o arquivo .csv a ser escorado.

```
python score-it.py example.csv
```
ou

```
python score-it.py C:\Documents\example.csv
```

**Certifique-se** de que o arquivo está usando `;` como separador e que ele **possua um header** informando o nome das colunas.

Depois de executado, será criado um arquivo no mesmo local chamado `{NomeDoArquivo}_4KSTd.csv` com três colunas adicionais:
- 4KST_ITEM_SCORE: Conterá o score do item, sendo um valor de **0 a 999**.
- 4KST_GUIA_SCORE: Conterá o score da guia, sendo um valor de **0 a 999**.
- GUIA_STATUS: Status da guia.

O arquivo de saída poderá ser maior que o de entrada devido as colunas adicionas. Mas também poderá ser menor, devido aos códigos de erros e prestadores filtrados, os quais o modelo não processa.