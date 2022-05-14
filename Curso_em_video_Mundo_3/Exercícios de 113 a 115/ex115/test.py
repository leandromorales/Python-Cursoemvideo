

def verifica_arquivo(nome):
    try:
        arquivo = open(nome, 'r')
    except FileNotFoundError:
        return False
    else:
        arquivo.close()
        return True


def cria_arquivo(nome):
    arquivo = open(nome, 'a')
    arquivo.close()


def ler_arquivo(nome):
    arquivo = open(nome, 'r')
    print(arquivo.read())
    arquivo.close()

#if verifica_arquivo() == True:
#    print('Arquivo existe.')
#else:
#    print('Arquivo não existe.')

if not verifica_arquivo('cadastro1.txt'):
    cria_arquivo('cadastro1.txt')
    print('Arquivo cadastro1.txt foi criado.')

ler_arquivo('cadastro1.txt')