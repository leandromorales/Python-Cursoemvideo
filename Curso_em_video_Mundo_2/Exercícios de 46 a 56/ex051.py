#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
termo = int(input('Digite o primeiro termo da progressão aritmética: '))
razao = int(input('Digite a razão: '))
for c in range(1, 11):
    if c == 1:
        print('{} termo da PA igual a {}.'.format(c, termo))
    else:
        termo += razao
        print('{} termo da PA igual a {}.'.format(c, termo))