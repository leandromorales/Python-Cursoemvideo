'''Adapte o código do desafio 107, criando uma função adicional chamada utilidadesCeV() que consiga
mostrar os valores como um valor monetário formatado.'''

from ex108 import moeda

p = float(input('Digite o preço: R$'))
metade = moeda.metade(p)
dobro = moeda.dobro(p)
aument = moeda.aumentar(p, 10)
dimin = moeda.diminuir(p, 10)
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(metade)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(dobro)}')
print(f'Aumentando 10%, temos {moeda.moeda(aument)}')
print(f'Diminuindo 10%, temos {moeda.moeda(dimin)}')