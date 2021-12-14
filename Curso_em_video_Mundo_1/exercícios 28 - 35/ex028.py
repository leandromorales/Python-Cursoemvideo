#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o
#usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import shuffle
lista = [0, 1, 2, 3, 4, 5]
shuffle(lista)
esc = int(lista[0])
#print(esc)
tentativa = int(input('Tente adivinhar o número de 0 a 5: '))
if tentativa == esc:
    print('Você acertou. O número gerado foi {}'.format(esc))
else:
    print('Você errou. O número gerado foi {}'.format(esc))