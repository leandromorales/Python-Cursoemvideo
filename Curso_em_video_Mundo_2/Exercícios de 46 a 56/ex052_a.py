#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
#Divisíveis apenas por 1 e por ele mesmo.
#Para identificar um número primo devemos dividi-lo sucessivamente por números primos como: 2, 3, 5. . . e verificar se a divisão é exata (em que o resto é zero) ou não exata (onde o resto é diferente de zero).
# - Se o resto da divisão for zero o número não é primo.
# - Se nenhum resto for zero, o número é primo.
tot = 0
num = int(input('Digite um número: '))
for c in range(1, num + 1):
    if num % c == 0:
        tot += 1
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes e '.format(num, tot), end='')
if tot == 2:
    print('é um número primo.')
else:
    print('não é um número primo.')
