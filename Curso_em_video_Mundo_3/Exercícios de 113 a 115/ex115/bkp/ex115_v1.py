'''Crie um pequeno sistema modularizado que permita cadastrar pessoeas pelo seu nome e idade em um
arquivo de texto simples.
O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.'''

from lib.interface import *
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        cabeçalho('Opção 1')
    elif resposta == 2:
        cabeçalho('Opção 2')
    elif resposta == 3:
        cabeçalho('Saindo do sistema.')
        break
    else:
        print('ERRO! Digite uma opção válida.')

