'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas;
B) A média de idade do grupo;
C) Uma lista com todas as mulheres;
D) Uma lista com todas as pessoas com idade acima da média.'''

censo = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).capitalize()
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    censo.append(pessoa.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Digite apenas S ou N.')
    if resp in 'N':
        break
print('-=' * 30)
print(f'A) Foram cadastradas {len(censo)} pessoas.')
media = soma / len(censo)
print(f'B) A média de idade é {media:.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for a in censo:
    if a['sexo'] == 'F':
        print(f'{a["nome"]} ', end='')
print()
print(f'D) Lista das pessoas que estão acima da média de idade:')
for a in censo:
    if a['idade'] > media:
        for b, c in a.items():
            print(f'{b} = {c}; ', end='')
        print()
print('<<ENCERRADO>>')

