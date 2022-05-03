
def aumentar(n=0, aum=0):
    por = n / aum
    fim = n + por
    return fim


def diminuir(n=0, dim=0):
    por = n / dim
    fim = n - por
    return fim


def dobro(n=0):
    return n * 2


def metade(n=0):
    return n / 2


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:>.2f}'.replace('.', ',')
