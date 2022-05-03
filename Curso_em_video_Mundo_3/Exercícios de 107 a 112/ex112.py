'''Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma
validação de dados para aceitar apenas valores que sejam monetários.'''

from ex112.utilidadesCeV.moeda import moedas
from ex112.utilidadesCeV.dado import valor

p = valor('Digite o preço R$: ')
moedas.resumo(p, 50, 50)
