# Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que
# quer mostrar 0 termos.

from time import sleep

termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
cont = 0
end = 1
final = int(input('''Digite a quantidade de termos que você quer visualizar ou 
Digite 0 para encerrar o programa: '''))
while cont <= final and end != 0:
    if final == 0:
        print('O programa será encerrado.')
        sleep(2)
        break
    if cont == final:
        end = int(input('\nDigite [0] para encerrar o programa ou digite quantos valores deseja exibir a mais?: '))
        if end == 0:
            print('O programa será encerrado.')
        else:
            final = end + 1
    else:
        print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
