'''Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função utilidadesCeV(), desenvolvida no
desafio 108.'''

from ex109 import moedas

p = float(input('Digite o preço: R$:'))
print(f'A metade de {moedas.moeda(p)} é {moedas.metade(p,True)}')
print(f'O dobro de {moedas.moeda(p)} é {moedas.dobro(p, True)}')
print(f'Aumentando 10%, temos {moedas.aumentar(p, 10, True)}')
print(f'Diminuindo 10%, temos {moedas.diminuir(p, 10, True)}')