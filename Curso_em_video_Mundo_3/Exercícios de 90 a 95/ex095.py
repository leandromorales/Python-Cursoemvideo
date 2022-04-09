'''Aprimore o desafio 93 para que ele funcione com vários jogadores, incluíndo um sistema
de visualização de detalhes do aproveitamento de cada jogador.'''

jogador = dict()
geral = list()
gols = list()
while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = str(input('Nome do Jogador: ')).capitalize()
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, jogador['partidas']):
        gols.append(int(input(f'Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    geral.append(jogador.copy())
    while True:
        choice = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if choice in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if choice == 'N':
        break

print('-=' * 30)
print(f'{"Cod":<4}{"Nome":<12}{"Gols":<22}{"Total":>10}')
print('-' * 60)
for x, y in enumerate(geral):
    print(f'{x:<4}{y["nome"]:<12}{y["gols"]}{y["total"]:>22}')
#for x, y in enumerate(geral):
print('-' * 60)
#print(len(geral))
while True:
    exi = int(input('Mostrar os resultados de qual jogador? (999 para parar): '))
    if exi == 999:
        print('O programa está sendo encerrado.')
        break
    elif exi > (len(geral) -1):
        print('ERRO! Jogador inválido.')
    else:
        print(f'  --  LEVANTAMENTO DO JOGADOR {geral[exi]["nome"]}:')
        #print(len(geral[exi]["gols"]))
        #print(geral[exi]["gols"][1])
        for i in range(0, len(geral[exi]["gols"])):
            print(f'  No jogo {i + 1} fez {geral[exi]["gols"][i]} gols.')