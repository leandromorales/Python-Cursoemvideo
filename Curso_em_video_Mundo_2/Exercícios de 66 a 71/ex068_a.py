# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
# quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final
# do jogo.

from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(1, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}. ', end='')
    print('Deu par' if total % 2 == 0 else 'Deu impar')
    if tipo == 'P':
        if total % 2 ==0:
            print('Você Venceu!')
            v += 1
        else:
            print('Você Perdeu!')
            break
    elif tipo == 'I':
        if total == 1:
            print('Você Venceu!')
            v += 1
        else:
            print('Você Perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'Game Over. Você venceu {v} vezes.')