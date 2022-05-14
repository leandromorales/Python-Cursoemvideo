
def verifica_arquivo(aqv):
    try:
        arquivo = open(aqv, 'rt')
    except FileNotFoundError:
        return False
    else:
        arquivo.close()
        return True


def cria_arquivo(aqv):
    arquivo = open(aqv, 'wt+')
    arquivo.close()


def ler_arquivo(aqv):
    arquivo = open(aqv, 'rt')
    print(arquivo.read())
    arquivo.close()


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

#https://wiki.python.org.br/ManipulandoStringsComPython
#https://www.tutorialspoint.com/python3/string_isalpha.htm


def leiaString(msg):
    while True:
        try:
            n = str(input(msg))
            if not n.is:
                print('\033[31mErro: Por favor, digite um nome válido.\033[m')
                continue
        except (ValueError, TypeError):
            print('\033[31mErro: Por favor, digite um nome válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar.\033[m')
            return 0
        else:
            return n


def gravar_arquivo(aqv):
    nome = leiaString('Nome: ')
    idade = leiaInt('Idade: ')
    arquivo = open(aqv, 'a+')
    arquivo.write(f'\n{nome}, {idade}')
    arquivo.close()
    print(f'Novo registro de {nome} adicionado.')