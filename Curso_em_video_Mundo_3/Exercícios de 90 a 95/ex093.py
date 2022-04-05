'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa
vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols
feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluíndo o total
de gols feitos durante o campeonato.'''

apv = dict()
gols = list()
total = 0
apv['Nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {apv["Nome"]} jogou: '))

for i in range(0, partidas):
    gol = int(input(f'Quantos gols na partida {i}? '))
    total += gol
    gols.append(gol)
apv['Gols'] = gols[:]
apv['Total'] = total

print('-=' * 30)
print(apv)
print('-=' * 30)
for x, y in apv.items():
    print(f'O campo {x} tem o valor {y}')
print('-=' * 30)
print(f'O jogador {apv["Nome"]} jogou {partidas} partidas.')
for x, y in enumerate(apv['Gols']):
    print(f'=> Na partida {x} fez {y} gols.')