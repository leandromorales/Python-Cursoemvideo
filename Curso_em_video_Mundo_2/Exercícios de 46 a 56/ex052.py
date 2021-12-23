#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
#Divisíveis apenas por 1 e por ele mesmo.
#Para identificar um número primo devemos dividi-lo sucessivamente por números primos como: 2, 3, 5. . . e verificar se a divisão é exata (em que o resto é zero) ou não exata (onde o resto é diferente de zero).
# - Se o resto da divisão for zero o número não é primo.
# - Se nenhum resto for zero, o número é primo.

num = int(input('Digite um número inteiro: '))
if num != 1 and num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 11 != 0:
    print('O número {} é um número primo.'.format(num))
else:
    print('O número {} não é um número primo.'.format(num))