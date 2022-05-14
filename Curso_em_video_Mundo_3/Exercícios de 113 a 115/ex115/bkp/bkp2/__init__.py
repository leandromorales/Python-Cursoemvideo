
from time import sleep


def linha(tam=30):
    print('-' * tam)


def validar_ent(msg):
    while True:
        try:
            n = int(input(msg))
        except ValueError:
            print('Erro! Digite um número inteiro válido.')
            continue
        else:
            return n


def menu(lista):
    cabeçalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    linha()
    opc = validar_ent('Sua opção: ')
    sleep(2)
    return opc


def cabeçalho(msg):
    print('-' * 30)
    print(msg.center(30))
    print('-' * 30)


def verifica_arquivo(nome):
    try:
        arquivo = open(nome, 'rt')
    except FileNotFoundError:
        return False
    else:
        arquivo.close()
        return True


def cria_arquivo(nome):
    arquivo = open(nome, 'wt+')
    arquivo.close()


def ler_arquivo(nome):
    arquivo = open(nome, 'rt')
    print(arquivo.read())
    arquivo.close()
