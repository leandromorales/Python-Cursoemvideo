'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados;
B) A soma dos valores da terceira coluna;
C) O maior valor da segunda linha.'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = 0
soma3 = 0
max2 = []
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somap += matriz[l][c]
        if c == 2:
            soma3 += matriz[l][c]

    print()
print(f'A soma dos valores pares é igual a {somap}')
print(f'A soma dos valores da terceira coluna é igual a {soma3}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')