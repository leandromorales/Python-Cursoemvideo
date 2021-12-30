# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5x4x3x2x1 = 120

num = int(input('Digite um número: '))
cont = num
fat = num
while cont > 1:
    cont = cont - 1
    fat = fat * cont
print('O Fatorial de {} é igual a {}.'.format(num, fat))
