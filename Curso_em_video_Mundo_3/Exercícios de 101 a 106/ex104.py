'''Crie um programa que tenha uma função chamada leiaint(), que vai fucnionar de forma semelhante à
função input() do Python, só que fazendo a validação para aceitar apenas valor numérico.
Ex:
n = leiaint('Digite um n')'''


def LeiaInt(num):
    while True:
        tst = input(num)
        if tst.isdigit():
            tst = int(tst)
            break
        else:
            #print('ERRO! Digite um número inteiro válido.')
            print(f'\033[0;31mERRO! Digite um número inteiro válido.\033[m')
    return tst


n = LeiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')