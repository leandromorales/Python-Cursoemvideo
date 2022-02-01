'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os
em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

nums = list()
while True:
    num = int(input('Digite um número: '))
    if num not in nums:
        nums.append(num)
        print('Número adicionado.')
    else:
        print(f'O número {num} já foi digitado. Não será adicionado.')
    cont = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if cont in 'N':
        break

fim = sorted(nums)

print(f'Os números digitados foram: ', end='')
for c in range(0, len(fim)):
    print(f'{fim[c]} ', end='')


