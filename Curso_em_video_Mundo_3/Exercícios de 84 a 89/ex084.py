'''Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas;
B) Uma listagem com as pessoas mais pesadas;
C) Uma listagem com as pessoas mais leves.'''


pesos = list()
final = list()
while True:
    pesos.append(str(input('Nome: ')))
    pesos.append(float(input('Peso: ')))
    final.append(pesos[:])
    pesos.clear()
    cont = str(input('Deseja continuar? [S/N]: '))
    if cont in 'Nn':
        break

maior = ''
menor = ''
maiores = list()
menores = list()

for c in range(0, len(final)):
    if c == 0:
        maior = menor = final[c][1]
    if final[c][1] > maior:
        maior = final[c][1]
    if final[c][1] < menor:
        menor = final[c][1]

for c in range(0, len(final)):
    if final[c][1] == maior:
        maiores.append(final[c][0])
    if final[c][1] == menor:
        menores.append(final[c][0])

print(f'Foram cadastradas {len(final)} pessoas.')
print(f'As pessoas mais pesadas são: {maiores}, com {maior}KG.')
print(f'As pessoas mais leves são: {menores}, com {menor}KG.')
