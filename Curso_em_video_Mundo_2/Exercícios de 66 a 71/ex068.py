# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
# quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final
# do jogo.

from random import randint
cont = 0
while True:
    num = int(input('Escolha um número: '))
    esc = str(input('[P/I]: '))
    numpc = randint(1, 11)
    total = numpc + num
    print(f'Você jogou {num} e o computador jogou {numpc}. Total de {total}. ', end='')

    if esc in 'Pp':
        if (numpc + num) % 2 == 0:
            print('Você ganhou!')
            cont += 1
        else:
            print('Você perdeu!')
            break
    if esc in 'Ii':
        if (numpc + num) % 2 == 0:
            print('Você perdeu!')
            break
        else:
            print('Você ganhou!')
            cont += 1

if cont == 0:
    print('Você não ganhou nenhuma vez.')
else:
    print(f'Você ganhou {cont} vezes.')



