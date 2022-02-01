'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os
em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado. Não será adicionado.')

    r = str(input('Quer continuar? [S/N] ')).strip().upper()
    if r in 'N':
        break
números.sort()
print(f'Você digitou os valores {números}')