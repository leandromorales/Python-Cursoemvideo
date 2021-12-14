#Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.

num = int(input('Digite um número inteiro: '))
calc = num % 2
if calc == 0:
    print('O número {} é par.'.format(num))
else:
    print('O número {} é impar.'.format(num))
print('Fim.')