# Melhore o jogo do Desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 10 e peça para o
# usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
sort = randint(0, 10)
print('Bem vindo ao jogo de advinhação.')
print('O computador está escolhendo um número...')
sleep(3)
cont = 1
tent = int(input('Tente adivinhar o número que o computador escolheu de 1 a 10: '))
while sort != tent:
    tent = int(input('Você errou. Tente novamente.\n Tente adivinhar o número que o computador escolheu de 1 a 10: '))
    cont += 1
print('Você acertou. O computador escolheu o número {}.\nForam necessárias {} tentativas.'.format(sort, cont))
