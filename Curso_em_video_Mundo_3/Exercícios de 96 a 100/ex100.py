''' Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somapar().
A primeira vai sortear 5 números e colocá-los dentro de uma lista e a segunda função vai mostrar a soma entre todos os
valores PARES sorteados pela função anterior.'''

from random import randint
from time import sleep

def sorteio():
    print('Sorteando 5 valores da lista: ', end='')
    sleep(0.5)
    sort = list()
    for c in range(0, 5):
        num = randint(0, 100)
        print(f'{num} ', end='')
        sleep(0.5)
        sort.append(num)
    print('Pronto')
    return sort

def somapar(lista):
    print(f'Somando os valores pares de {lista}, ', end='')
    sleep(0.5)
    soma = 0
    for c, d in enumerate(lista):
        if lista[c] % 2 == 0:
            soma += d
    print(f'Temos {soma}.')


#Código principal
numeros = sorteio()
somapar(numeros)