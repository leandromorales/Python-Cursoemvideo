'''Reescreva a função leiaint() que fizemos no desafio 104, incluíndo agora a possibilidade
de digitação de um número de tipo inválido. Aproveite e crie uma função leiaFloat() com a
mesma funcionalidade.'''

def leiaint(msg):
    while True:
        n = input(msg)
        try:
            n = int(n)
            break
        except ValueError:
                print(f'\033[0;31mERRO! Por favor, digite um número inteiro válido.\033[m')
    return n

def leiafloat(msg):
    while True:
        n = input(msg).replace(',', '.')
        try:
            n = float(n)
            break
        except ValueError:
                print(f'\033[0;31mERRO! Por favor, digite um número real válido.\033[m')
    return n

ni = leiaint('Digite um inteiro: ')
nr = leiafloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {ni} e o real foi {nr}.')
