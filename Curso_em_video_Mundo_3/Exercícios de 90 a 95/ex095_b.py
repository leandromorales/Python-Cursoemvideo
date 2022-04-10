'''Aprimore o desafio 93 para que ele funcione com vários jogadores, incluíndo um sistema
de visualização de detalhes do aproveitamento de cada jogador.'''

jogador = dict()
geral = list()
gols = list()
soma = 0
while True:
    jogador.clear()
    gols.clear()
    jogador['Nome'] = str(input('Nome do jogador: ')).capitalize()
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for i in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {i + 1}? ')))

    jogador['Gols'] = gols[:]
    jogador['Total'] = sum(gols)
    geral.append(jogador.copy())
    while True:
        choice = str(input('Deseja continuar? [S/N]: ')).upper()[0]
        if choice not in 'SN':
            print('ERRO! Digite somente S ou N! ')
        else:
            break
    if choice == 'N':
        break
#print(geral)
print('-=' * 30)
print(f'{"Cod ":<3}', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for i, j in enumerate(geral):
    print(f'{i:<3} ',end='')
    for a in j.values():
        print(f'{str(a):<15}', end='')
    print()
print('-' * 40)
print()
while True:
    esc = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if esc == 999:
        break
    if esc >= len(geral):
        print(f'ERRO! Jogador {esc} não encontrado.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {geral[esc]["Nome"]}')
        for i, j in enumerate(geral[esc]["Gols"]):
            print(f'  No jogo {i + 1} fez {j} gols.')
print('<<VOLTE SEMPRE>>')
