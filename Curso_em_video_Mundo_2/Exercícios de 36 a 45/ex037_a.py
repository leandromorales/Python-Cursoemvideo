#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

num = int(input("Digite um número para ser convertido: "))

cont = 3

while cont > 0:
    base = int(input('''Escolha uma base para conversão:
    [ 1 ] - Binário
    [ 2 ] - Octal
    [ 3 ] - Hexadecimal
    :::: Sua opção: '''))

    if base == 1:
        cont = 0
        print('{} convertido par Binário é igual a {}.'.format(num, bin(num)[2:]))
    elif base == 2:
        cont = 0
        print('{} convertido para Octal é igual a {}.'.format(num, oct(num)[2:]))
    elif base == 3:
        cont = 0
        print('{} convertido para Hexadecimal é igual a {}.'.format(num, hex(num)[2:]))
    else:
        cont = cont - 1
        if cont > 0:
            print('Opção inválida, tente novamente.')
            print('{} tentativas restantes.'.format(cont))
        else:
            print('Opção inválida. O programa será encerrado.')