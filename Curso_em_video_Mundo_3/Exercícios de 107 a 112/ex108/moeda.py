
def aumentar(n, aum):
    por = n * (aum/100)
    fim = n + por
    return fim


def diminuir(n, dim):
    por = n * (dim/100)
    fim = n - por
    return fim


def dobro(n):
    return n * 2


def metade(n):
    return n / 2


def moeda(n):
    import locale
    locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
    format = locale.currency(n, grouping=True)
    return format
