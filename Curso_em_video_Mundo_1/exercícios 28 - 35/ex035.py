#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se ele pode
#ou não formar um triângulo.

l1 = float(input('Digite o comprimento da primeira reta: '))
l2 = float(input('Digite o comprimento da segunda reta: '))
l3 = float(input('Digite o comprimento da terceira reta: '))

if l1 + l2 == l3 or l1 + l3 == l2:
    print('Estas retas não formam um triângulo.')
else:
    print('Estas retas formam um triângulo.')

#https://brasilescola.uol.com.br/o-que-e/matematica/o-que-e-a-condicao-existencia-um-triangulo.htm