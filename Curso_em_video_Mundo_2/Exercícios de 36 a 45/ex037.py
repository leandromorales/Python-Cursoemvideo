#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

#Tipo de formatação	Papel
#=	Coloca o sinal na posição mais à esquerda
#b	Converte o valor em binário equivalente
#o	Converte o valor para o formato octal
#x	Converte o valor para o formato Hex
#d	Converte o valor dado em decimal
#E	Formato científico, com um E em maiúsculas
#X	Converte o valor para o formato Hex em maiúsculas
#
num = int(input('Digite um número para ser convertido: '))

ctrl = 0
while ctrl == 0:
    base = int(input('''Escolha a base numérica para conversão:
    1 - Binário;
    2 - Octal;
    3 - Hexadecimal.
    :'''))

    if base == 1:
        ctrl = 1
        num_bin = format(num, 'b')
        print('O número decimal "{}" fica "{}" convertido para binário.'.format(num, num_bin))
    elif base == 2:
        ctrl = 1
        num_oct = format(num, 'o')
        print('O número decimal "{}" fica "{}" convertido para octal.'.format(num, num_oct))
    elif base == 3:
        ctrl = 1
        num_hex = format(num, 'X')
        print('O número decimal "{}" fica "{}" convertido para octal'.format(num, num_hex))
    else:
        ctrl = 0
        print('opção inválida')




