# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado(número inteiro) e o programa vai
# informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('{:-^40}'.format('Caixa Eletronico'))
while True:
    valor = float(input('Qual valor será sacado? R$'))
    n50 = n20 = n10 = n1 = 0
    if valor > 50:
        n50 = valor // 50
        resto = valor % 50
        valor = resto
    if valor >= 20:
        n20 = valor // 20
        resto = valor % 20
        valor = resto
    if valor >= 10:
        n10 = valor // 10
        resto = valor %10
        valor = resto
    if valor >= 1:
        n1 = valor // 1

    print('Serão entregues:')
    if n50 != 0:
        print(f'{n50:.0f} notas de R$50;')
    if n20 != 0:
        print(f'{n20:.0f} notas de R$20;')
    if n10 != 0:
        print(f'{n10:.0f} notas de R$10;')
    if n1 != 0:
        print(f'{n1:.0f} notas de R$1.')

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja fazer um novo saque? [S/N]: ')).strip().upper()[0]
    if resp =='N':
        break

print('{:-^40}'.format('Fim'))
