'''Crie um módulo chamado moedas.py que tenha as funções incorporadas aumentar(),
diminuir(), dobro() e metade().

Faça também um programa que importe esse módulo e use algumas dessas funções.'''

from ex107_a import moeda


p = float(input('Digite o preço: R$:'))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de R${p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p, 10)}')
print(f'Diminuindo 10%, temos R${moeda.diminuir(p, 10)}')