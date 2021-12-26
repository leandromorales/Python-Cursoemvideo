# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
# Maioridade 21 anos."""

from datetime import date
maior = 0
menor = 0
# ano = 2017
ano = date.today().year
for c in range(1, 8):
    nasc = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    if ano - nasc >= 21:
        maior += 1
    else:
        menor += 1

print('Das pessoas listadas, {} são maiores e {} são menores.'.format(maior, menor))
