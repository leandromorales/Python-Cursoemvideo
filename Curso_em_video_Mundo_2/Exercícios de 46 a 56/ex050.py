#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que
# forem pares. Se o valor digitado for ímpar, desconsidere-o.
num1 = 0
cont = 0
for i in range(0, 6):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        num1 += num
        cont += 1

print('A soma dos {} valores pares digitados é igual a {}.'.format(cont, num1))