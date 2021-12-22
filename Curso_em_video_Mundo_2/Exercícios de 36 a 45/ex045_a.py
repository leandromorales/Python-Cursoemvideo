#Crie um programa que faça o computador jogar jokenpô com você.
#Regras:
#Tesoura corta papel
#Papel embrulha pedra
#Pedra quebra tesoura

from random import randint
itens = ('inicio', 'Pedra', 'Papel', 'Tesoura')
computador = randint(1, 3)

print('''Suas opções:
[ 1 ] Pedra;
[ 2 ] Papel;
[ 3 ] Tesoura.''')
jogador = int(input('Qual é a sua Jogada? '))
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))

if computador == 1:
    if jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Você ganhou!')
    elif jogador == 3:
        print('Você perdeu!')
elif computador == 2:
    if jogador == 1:
        print('Você Perdeu!')
    elif jogador == 2:
        print('Empate!')
    elif jogador == 3:
        print('Você ganhou!')
elif computador == 3:
    if jogador == 1:
        print('Você ganhou!')
    elif jogador == 2:
        print('Você perdeu!')
    elif jogador == 3:
        print('Empate!')
