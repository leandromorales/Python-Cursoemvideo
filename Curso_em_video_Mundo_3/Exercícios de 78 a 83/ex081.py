'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:

A) Quantos números foram digitados;
B) A lista de valores ordenada de forma decrescente;
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = []
num = ''
while True:
    while not num.isnumeric():
        num = input('Digite um número: ')
    lista.append(int(num))
    cont = str(input('Deseja continuar? [S/N]')).upper().strip()
    num = ''
    while cont not in 'SN':
        print('while')
        cont = str(input('Deseja continuar? [S/N]')).upper().strip()
        if cont == 'N':
            print('Break')
            break
            break
    print('Fora')
    cont = ''

print(f'Foram digitados {len(lista)} números.')
print(lista)