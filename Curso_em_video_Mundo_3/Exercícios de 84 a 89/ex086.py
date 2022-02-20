'''Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos
pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.'''

matriz = [[], [], []]

for c in range(0, 3):
    for g in range(0, 3):
        valor = int(input(f'Digite o valor da posição {c, g}: '))
        matriz[c].append(valor)

for c in range(0, 3):
    for g in range(0, 3):
        if g == 2:
            print(f'[{matriz[c][g]}]')
        else:
            print(f'[{matriz[c][g]}]', end='')
