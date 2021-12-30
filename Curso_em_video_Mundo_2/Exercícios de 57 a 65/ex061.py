# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

termo = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
cont = 1
while cont <= 10:
    if cont == 10:
        print('{} - Fim.'.format(termo))
    else:
        print('{} -> '.format(termo), end='')
    termo += razão
    cont += 1