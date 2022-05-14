'''Crie um pequeno sistema modularizado que permita cadastrar pessoeas pelo seu nome e idade em um
arquivo de texto simples.
O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.'''

from lib.interface import *
from lib.arquivo import *

aqv = 'cadastro.txt'

if not verifica_arquivo(aqv):
    cria_arquivo(aqv)
    print(f'Arquivo {aqv} foi criado.')

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        cabeçalho('Opção 1')
        ler_arquivo(aqv)
        sleep(1)
    elif resposta == 2:
        cabeçalho('Opção 2')
        gravar_arquivo(aqv)
    elif resposta == 3:
        cabeçalho('Saindo do sistema.')
        break
    else:
        print('ERRO! Digite uma opção válida.')


