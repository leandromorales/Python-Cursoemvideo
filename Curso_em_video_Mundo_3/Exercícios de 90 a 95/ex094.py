'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas;
B) A média de idade do grupo;
C) Uma lista com todas as mulheres;
D) Uma lista com todas as pessoas com idade acima da média.'''

censo = list()
pessoa = dict()
med = 0
while True:
    pessoa['nome'] = str(input('Nome: ')).capitalize()
    pessoa['sexo'] = 'a'
    cont = 0
    while pessoa['sexo'] not in 'MmFf':
        if cont > 0:
            print('Erro! Por favor, digite apenas M ou F.')
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()
        cont += 1
    pessoa['idade'] = int(input('Idade: '))
    med += pessoa['idade']
    censo.append(pessoa.copy())
    ag = 'a'
    cont = 0
    while ag not in 'SsNn':
        if cont > 0:
            print('Erro! Digite apenas S ou N.')
        ag = str(input('Deseja continuar? [S/N]: '))
        cont += 1
    if ag.lower() == 'n':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(censo)} pessoas cadastradas.')
media = med / len(censo)
print(f'B) A média de idade é de {media:.2f}')
print(f'C) As mulheres cadastradas foram: ', end='')
for c in range(0, len(censo)):
    if censo[c]['sexo'] == 'F':
        print(f'{censo[c]["nome"]} ', end = '')
print()
print(f'D) Lista de pessoas que estão acima da média')
for g in range(0, len(censo)):
    if censo[g]['idade'] > media:
        print(f'Nome= {censo[g]["nome"]}; sexo= {censo[g]["sexo"]}; idade= {censo[g]["idade"]};')
print('<<ENCERRADO>>')






#print(pessoa)
#print(censo)