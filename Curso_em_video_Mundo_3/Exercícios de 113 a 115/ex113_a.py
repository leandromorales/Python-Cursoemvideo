'''Reescreva a função leiaint() que fizemos no desafio 104, incluíndo agora a possibilidade
de digitação de um número de tipo inválido. Aproveite e crie uma função leiaFloat() com a
mesma funcionalidade.'''

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: Por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar este número.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: Por favor, digite um número real válido.\033m')
            continue
        except (KeyboardInterrupt):
            print('\033[mUsuário preferiu não digitar este número.\033[m')
            return 0
        else:
            return n


n1 = leiaInt('Digite um valor: ')
n2 = leiaFloat('Digite um real: ')
print(f'O valor inteiro digitado foi {n1} e o valor real digitado foi {n2}.')