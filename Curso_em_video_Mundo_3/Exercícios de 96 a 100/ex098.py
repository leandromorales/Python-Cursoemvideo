''' Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e
realiza a contagem.
Seu programa tem que realizar três contagens através da função criada:
A) De 1 até 10, de 1 em 1;
B) De 10 até 0, de 2 em 2;
C) Uma contagem personalizada.

'''
from time import sleep
def contadora(inicio, fim, passo):
    print(f'Contagem de {inicio} a {fim} com passo de {passo}: ', end='')
    if passo > 0:
        fim += 1
    else:
        fim -= 1
    for c in range(inicio, fim, passo):
        print(f' {c}', end='')
    print()

def contador(inicio, fim, passo):
    if passo <0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} a {fim} com passo de {passo}: ', end='')
    sleep(2.5)
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += passo
        print('FIM')

    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= passo
        print('FIM')


contador(1, 10, 1)
contador(10, 0, -2)
while True:
    while True:
        esc = str(input('Deseja personalizar uma contagem? [S/N]: ')).upper()[0]
        if esc in 'SN':
            break
        else:
            print('Opção incorreta.')
    if esc == 'N':
        break
    else:
        inicio = int(input('Digite o inicio da contagem: '))
        fim = int(input('Digite o fim da contagem: '))
        passo = int(input('Digite o passo da contagem: '))
        contador(inicio, fim, passo)
print('Fim do programa.')