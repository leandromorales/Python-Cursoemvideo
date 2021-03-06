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
for c in range(0, 5):
    print(tabela[c], end=' ')
print('')
print('=' * 30)
print('Os quatro últimos colocados na tabela são: ')
for d in range(-16, -20):
    print(d)