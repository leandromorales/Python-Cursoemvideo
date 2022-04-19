''' Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

'''
from time import sleep

def maior(* num):
    lista = list()
    print('-=' * 30)
    print(' Analisando os números informados: ')
    for c in num:
        lista.append(c)
        print(f' {c}', end='')
        sleep(0.5)
    print()
    if len(lista) == 0:
        print('Não foram informados números.')
    else:
        print(f' Foram informados {len(lista)} números.')
        print(f' O maior número é {max(lista)}.')




#Código principal

maior(1, 5, 22)
maior()
maior(12, 3, 54, 8)
maior(25, 583, 1589, 125487)
