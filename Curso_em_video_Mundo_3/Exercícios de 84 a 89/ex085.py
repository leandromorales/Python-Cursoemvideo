'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
em uma lista única que mantenha os valores pares e ímpares. No final, mostre os valores pares e
ímpares em ordem crescente.'''

valores = list()

for c in range(1, 8):
    valores.append(int(input(f'Digite o {c}º número: ')))
valores = sorted(valores)

print('Números pares digitados: ')
for c in range(0, 7):
    if valores[c] % 2 == 0:
        print(f'{valores[c]} ', end='')

print()
print('Números ímpares digitados: ')
for c in range(0, 7):
    if valores[c] % 2 != 0:
        print(f'{valores[c]} ', end='')