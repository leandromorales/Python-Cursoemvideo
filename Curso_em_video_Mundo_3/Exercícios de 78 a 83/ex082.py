'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores
ímpares digitados, respectivamente.
Ao final, mostre o resultado das três listas geradas.'''

valores = []
par = []
imp = []
num = ''
while True:
    while not num.isnumeric():
        num = input('Digite um número: ')
    numm = int(num)
    valores.append(numm)
    if numm % 2 == 0:
        par.append(numm)
    else:
        imp.append(numm)
    num = ''
    cont = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while cont != 'S' and cont != 'N':
        cont = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if cont == 'N':
        break
print(f'Os números digitados foram: {valores}')
print(f'Entre os números digitados, estes são pares {par},')
print(f'e estes são ímpares {imp}')