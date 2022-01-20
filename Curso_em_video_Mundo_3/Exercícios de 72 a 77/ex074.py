'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
mostre a listagem de números gerados e também indique o menor e o maior valor que estão na
tupla
'''
from random import randint

sorteio = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), )
print(f'Os números sorteados foram: {sorteio}')

maior = ''
menor = ''

for c in range(0, 5):
    num = sorteio[c]
    if c == 0:
        menor = num
        maior = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(f'O maior número digitado foi: {maior}')
print(f'O menor número digitado foi: {menor}')

