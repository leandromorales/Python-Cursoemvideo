'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo
que o vencedor tirou o maior número no dado.'''

from random import randint
from time import sleep
dado = ''
jogadas = dict()
for c in range(1, 5):
    dado = randint(1, 6)
    print(f'Jogador {c} tirou {dado} no dado.')
    jogadas[f'jogador {c}'] = dado
    sleep(1)
#print(jogadas)

print('-=' * 30)
print('== Ranking dos jogadores ==')
cont = 1

for i in sorted(jogadas, key = jogadas.get, reverse=True):
    print(f'{cont}º lugar: {i} com {jogadas[i]}.')
    cont += 1

'''for a in sorted(jogadas, key= jogadas.get, reverse=True):
    print(f'{cont} lugar {a} com {jogadas[a]}.')
    cont += 1'''

'''for i in sorted(jogadas, key = jogadas.get, reverse=True):
    print(i, jogadas[i])'''
print('FIM')