'''Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moedas e dado.
Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha
 tudo funcionando.'''



from ex112_a.utilidadescev import moedas
from ex112_a.utilidadescev import dado

p = dado.leiaDinheiro('Digite o preço R$: ')
moedas.resumo(p, 10, 5)
