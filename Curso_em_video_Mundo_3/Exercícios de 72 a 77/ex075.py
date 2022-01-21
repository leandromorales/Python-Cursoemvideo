'''
Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A - Quantas vezes apareceu o número 9;
B - Em que posição apareceu o número 3;
C - Quais foram os números pares.

'''

valores = (int(input('Digite o primeiro valor: ')), int(input('Digite o segundo valor: ')),
           int(input('Digite o terceiro valor: ')), int(input('Digite o quarto valor: ')))

print('-=' * 30)
if valores.count(9) == 0:
    print(f'O número 9 não foi digitado.')
else:
    print(f'O número 9 apareceu {valores.count(9)} vezes.')
#print(valores)

print('-=' * 30)
if valores.count(3) == 0:
    print(f'O número 3 não foi digitado.')
else:
    print(f'O número 3 apareceu na posição {valores.index(3)}.')

print('-=' * 30)
print('Os pares digitados foram:  ')
veri = 0
for c in valores:
    if c % 2 == 0:
        print(c, end=' ')

