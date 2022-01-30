'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

valores = list()

for c in range(0, 5):
    valores.append(int(input(f'Digite o {c + 1}º valor: ')))
print(valores)

print(f'O maior valor digitado é: {max(valores)}, nas posições: ', end='')
for i, c in enumerate(valores):
    if c == max(valores):
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado é: {min(valores)}, nas posições: ', end='')
for i, c in enumerate(valores):
    if c == min(valores):
        print(f'{i}...', end='')
print()

