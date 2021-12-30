# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5x4x3x2x1 = 120

num = int(input('Digite um número para calcular o seu fatorial: '))
fat = 1
cont = num
for c in range(num, 1, -1):
    fat *= cont
    cont -= 1
    #print(fat)

print('O Fatorial de {} é {}.'.format(num, fat))
