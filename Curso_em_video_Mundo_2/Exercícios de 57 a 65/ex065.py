# Crie um programa que leia vários números inteiros pelo teclado. No final da execuçao, mostre a média entre todos os valores
# e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

num = int(input('Digite um número: '))
ctrl = 'S'
cont = 0
maior = num
menor = num
soma = 0
while ctrl not in 'Nn':
    if cont != 0:
        num = int(input('Digite um número: '))
    soma += num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    cont += 1
    ctrl = str(input('Deseja continuar? [S/N]: '))
med = soma / cont
print('A média dos {} valores digitados é: {:.2f}'.format(cont, med))
print('O maior valor digitado foi {} e o menor valor digitado foi {}.'.format(maior, menor))
