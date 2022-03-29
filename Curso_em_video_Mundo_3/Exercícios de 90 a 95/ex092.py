'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os
(com idade) em um dicionário. Se por acaso a CTPS for diferente de zero, o dicionário receberá
também o ano da contratação e o salário. Calcule e acrescente, além da idade, com quantos anos
a pessoa vai se aposentar.'''
#35 anos de contribuição para se aposentar.
from datetime import date
#ano = date.today().year
ano = 2017
trab = dict()
trab['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
trab['idade'] = ano - nascimento
trab['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if trab['ctps'] != 0:
    trab['contratação'] = int(input('Ano de Contratação: '))
    trab['salário'] = float(input('Salário: '))
    trab['aposentadoria'] = (trab['contratação'] - nascimento) + 35

print('-=' * 30)
for x, y in trab.items():
    print(f'- {x} tem o valor {y}')




