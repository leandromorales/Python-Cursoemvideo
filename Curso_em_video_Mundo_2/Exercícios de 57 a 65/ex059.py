# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep



v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))
print('Processando...')
sleep(1)
msg = '''Digite uma opção para processar os valores:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Digitar novos número
[5] Exit
Sua opção: '''
menu = 0
cont = 0
while menu not in range(1, 5):
    menu = int(input(msg))
    if menu == 1:
        soma = v1 + v2
        sleep(1)
        print('A soma dos valores {} e {} é igual a {}.'.format(v1, v2, soma))
        menu = 0
        sleep(1)
    if menu == 2:
        multi = v1 * v2
        sleep(1)
        print('O produto entre os valores {} e {} é igual a {}.'.format(v1, v2, multi))
        menu = 0
        sleep(1)
    if menu == 3:
        maior = v1
        if v2 > v1:
            maior = v2
        print('O maior valor entre {} e {} é {}.'.format(v1, v2, maior))
        menu = 0
        sleep(1)
    if menu == 4:
        print('Você escolheu a opção 4 - Os valores serão solicitados novamente...')
        sleep(1)
        v1 = float(input('Digite o primeiro valor: '))
        v2 = float(input('Digite o segundo valor: '))
        menu = 0
        sleep(1)
    if menu == 5:
        print('O programa será encerrado.')
        sleep(1)
        break