#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma
# mensagem:
# - O primeiro valor é maior;
# - O segundo valor é maior:
# - não existe valor maior, os dois são iguais.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('O primeiro número digitado, "{}", é maior que o segundo número."{}"'.format(n1, n2))
elif n1 == n2:
    print('Os números digitados são iguais.')
else:
    print('O segundo número digitado, "{}" é maior que o primeiro número."{}"'.format(n2, n1))
