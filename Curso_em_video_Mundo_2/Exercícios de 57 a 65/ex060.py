# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5x4x3x2x1 = 120

num = int(input('Digite um número: '))
while num > 0:
    fat = num * (num - 1)
    num -= 1
print('O Fatorial de {} é igual a {}.'.format(num, fat))
