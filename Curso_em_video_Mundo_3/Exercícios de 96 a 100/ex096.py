'''Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.
'''

def area(a, b):
    terreno = a * b
    print(f'A área do terreno de {a}m X {b}m é de {terreno}m2.')

print('-' * 30)
print('Calculo de área')
lar = float(input('Digite a largura do terreno: '))
com = float(input('Digite o comprimento do terreno: '))
area(lar, com)

