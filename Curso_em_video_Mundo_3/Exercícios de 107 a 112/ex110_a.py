'''Adicione ao módulo moedas.py criado nos desafios anteriores, uma função chamada resumo(), que
mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.'''

from ex110_a import moedas

p = float(input('Digite o preço R$: '))
moedas.resumo(p, 10, 5)
