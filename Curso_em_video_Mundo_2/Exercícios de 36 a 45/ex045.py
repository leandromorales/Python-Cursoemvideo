#Crie um programa que faça o computador jogar jokenpô com você.
#Regras:
#Tesoura corta papel
#Papel embrulha pedra
#Pedra quebra tesoura

#import random
from random import randint
#ram = random.randint(1, 3)
ram = randint(1, 3)
#print(ram)

print('''Escolha sua opção:
[ 1 ] Pedra;
[ 2 ] Papel;
[ 3 ] Tesoura.''')
op = int(input('Sua opção: '))

if ram == 1:
    comp = 'Pedra'
    if op == 1:
        print('Computador escolheu Pedra. Empate!')
    elif op == 2:
        print('Computador escolheu Pedra. Papel embrulha Pedra. Você ganhou!')
    elif op == 3:
        print('Computador escolheu Pedra. Pedra quebra tesoura. Você perdeu!')
elif ram == 2:
    comp = 'Papel'
    if op == 1:
        print('Computador escolheu Papel. Papel embrulha Pedra. Você Perdeu!')
    elif op == 2:
        print('Computador escolheu Papel. Empate!')
    elif op == 3:
        print('Computador escolheu Papel. Tesoura corta papel. Você ganhou!')
elif ram == 3:
    comp = 'Tesoura'
    if op == 1:
        print('Computador escolheu Tesoura. Pedra quebra tesoura. Você ganhou!')
    elif op == 2:
        print('Computador escolheu Tesoura. Tesoura corta papel. Você perdeu!')
    elif op == 3:
        print('Computador escolheu Tesoura. Empate!')


