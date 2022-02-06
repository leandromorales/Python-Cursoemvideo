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
    num = ''
    cont = str(input('Deseja continuar? [S/N]')).strip().upper()
    if cont == 'N':
        break

print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse= True)
print(lista)
num = lista.count(5)
if num == 0:
    print('O número 5 não foi digitado.')
else:
    print(f'O número 5 foi digitado {num} vezes.')
