'''Crie um programa que tenha uma função chamada leiaint(), que vai fucnionar de forma semelhante à
função input() do Python, só que fazendo a validação para aceitar apenas valor numérico.
Ex:
n = leiaint('Digite um n')'''

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')