'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do campeonato brasileiro
de futebol, na ordem de colocação. Depois mostre:

A - Apenas os 5 primeiros colocados;
B - Os últimos 4 colocados da tabela;
C - Uma lista com os times em ordem alfabética;
D - Em que posição da tabela está o time da Chapecoense.
'''

tabela = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino',
'Fluminense', 'América-MG', 'Atlético-GO', 'Santos', 'Ceará', 'Internacional',
'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')

print('=' * 30)
print('Campeonato Brasileiro')

print('=' * 30)
print('Os cinco primeiros colocados na tabela são: ')
print(tabela[0:4])

print('=' * 30)
print('Os quatro últimos colocados na tabela são: ')
print(tabela[16:])

print('=' * 30)
print('Tabela em ordem alfabética: ')
print(sorted(tabela))

print('=' * 30)
print(f'O time da Chapecoense está na posição {enumerate(tabela[Chapecoense])}')