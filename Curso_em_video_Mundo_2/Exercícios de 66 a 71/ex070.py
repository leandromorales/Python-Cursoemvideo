# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar
# se o usuário vai continuar.
# No final, mostre:
# A - Qual é o total gasto na compra;
# B - Quantos produtos custam mais de R$1000;
# C - qual é o nome do produto mais barato.

tot = maism = menor = cont = 0
bar = ' '
while True:
    nprod = str(input('Digite o nome do produto: '))
    npre = float(input('Digite o preço R$: '))
    if npre < menor:
        bar = nprod
        menor = npre
    if npre > 1000:
        maism += 1
    tot += npre
    per = ' '
    while per not in 'SN':
        per = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if per == 'N':
        break
print(f'O total da compra é: R${tot:.2f}.')
print(f'O produto mais barato é {bar}, que custa R${menor:.2f}.')
if maism == 0:
    print('Nenhum produto digitado custa mais de R$1000,00.')
elif maism == 1:
    print('Somente um produto digitado custa mais de R$1000,00')
else:
    print(f'Foram digitados {maism} produtos com valor maior que R$1000,00.')
