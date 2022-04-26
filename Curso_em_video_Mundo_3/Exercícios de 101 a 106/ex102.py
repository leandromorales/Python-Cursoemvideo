'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique
o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado
ou não na tela o processo de cálculo do fatorial.'''

def fatorial(n, show=0):
    '''-> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.'''
    print('-' * 30)
    f = 1
    if show==True:
        for c in range(n, 0, -1):
            f *= c
            if c!=1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} = ', end='')
        return (f)
    else:
        for c in range(n, 0, -1):
            f *= c
        return (f)


help(fatorial)
print(fatorial(5, show=False))