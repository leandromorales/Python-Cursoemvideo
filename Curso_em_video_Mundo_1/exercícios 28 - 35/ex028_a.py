#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o
#usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

lista = randint(0, 5)

print(lista)
tent = int(input('Digite um número de "0" a "5":'))
print('processando...')
sleep(5)
if tent == lista:
    print('Você acertou! O número gerado pelo computador foi: {}.'.format(lista))
else:
    print('Você errou! O número gerado pelo computador foi: {}'.format(lista))