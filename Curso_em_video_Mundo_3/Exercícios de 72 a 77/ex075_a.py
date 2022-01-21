'''
Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A - Quantas vezes apareceu o número 9;
B - Em que posição apareceu o número 3;
C - Quais foram os números pares.

'''

núm = (int(input('Digite o primeiro valor: ')), int(input('Digite o segundo valor: ')),
           int(input('Digite o terceiro valor: ')), int(input('Digite o quarto valor: ')))

print(f'Você digitou os valores {núm}')
print(f'O valor 9 apareceu {núm.count(9)} vezes.')
if 3 in núm:
    print(f'O valor 3 apareceu na posição {núm.index(3)}.')
else:
    print('O número 3 não foi digitado.')
print('Os números pares digitados foram: ')
for n in núm:
    if n % 2 == 0:
        print(n, end=' ')
print('\nfim')