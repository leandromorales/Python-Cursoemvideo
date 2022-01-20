'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do campeonato brasileiro
de futebol, na ordem de colocação. Depois mostre:

A - Apenas os 5 primeiros colocados;
B - Os últimos 4 colocados da tabela;
C - Uma lista com os times em ordem alfabética;
D - Em que posição da tabela está o time da Chapecoense.
'''

times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino',
'Fluminense', 'América-MG', 'Atlético-GO', 'Santos', 'Ceará', 'Internacional',
'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')

print('-=' * 15)
print(f'Lista de times> {times}')
'''for t in times:
    print(t)'''

print('-=' * 15)
print(f'Os cinco primeiros são: {times[0:5]}')

print('-=' * 15)
print(f'Os quatro últimos são: {times[-4:]}')

print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')

print('-=' * 15)
print(f'O Chapecoense está na {times.index("Chapecoense") + 1}ª posição.')