#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

if num1 > num2 and num1 > num3:
    print('O número: {:.0f} é o maior número digitado.'.format(num1))
elif num2 > num1 and num2 > num3:
    print('O número: {:.0f} é o maior número digitado.'.format(num2))
elif num3 > num1 and num3 > num2:
    print('O número: {:.0f} é o maior número digitado.'.format(num3))

if num1 < num2 and num1 < num3:
    print('O número: {:.0f} é o menor número digitado.'.format(num1))
elif num2 < num1 and num2 < num3:
    print('O número: {:.0f} é o menor número digitado.'.format(num2))
elif num3 < num1 and num3 < num2:
    print('O número: {:.0f} é o nemor número digitado.'.format(num3))