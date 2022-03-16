'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um
dicionário. No final, mostre o conteúdo da estrutura na tela.'''

boletim = dict()
boletim['Nome'] = str(input('Nome: '))
boletim['Média'] = float(input('Média: '))
if boletim['Média'] >= 7:
    boletim['Situação'] = 'Aprovado'
else:
    boletim['Situação'] = 'Reprovado'

for k, v in boletim.items():
    print(f'- {k} é igual a {v}')

#print(boletim)