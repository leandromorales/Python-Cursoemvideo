# Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que
# quer mostrar 0 termos.

from time import sleep

termo = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
cont = 1
final = int(input('''Digite a quantidade de termos que você quer visualizar: 
Digite 0 para encerrar o programa: '''))
while cont <= final:
    if final == 0:
        print('O programa será encerrado.')
        sleep(2)
        break
    if cont == final:
        print('{} - Fim.'.format(termo))
    else:
        print('{} -> '.format(termo), end='')
    termo += razão
    cont += 1
