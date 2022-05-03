
def aumentar(n=0, aum=0, form=False):
    por = n * (aum/100)
    fim = n + por
    if form:
        return moeda(fim)
    else:
        return fim


def diminuir(n=0, dim=0, form=False):
    por = n * (dim/100)
    fim = n - por
    if form:
        return moeda(fim)
    else:
        return fim


def dobro(n=0, form=False):
    dobro = n * 2
    if form:
        return moeda(dobro)
    else:
        return dobro


def metade(n=0, form=False):
    metade = n / 2
    if form:
        return moeda(metade)
    else:
        return metade


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:>.2f}'.replace('.', ',')
