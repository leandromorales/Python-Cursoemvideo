'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
diminuir(), dobro() e metade().

Faça também um programa que importe esse módulo e use algumas dessas funções.'''


from ex107.moeda import metade, dobro, aumentar, diminuir
aum = 10
dim = 10
valor = float(input('Digite um preço: R$'))
print(f'A metade de R${valor} é R${metade(valor)}')
print(f'O dobro de R${valor} é R${dobro(valor)}')
print(f'Aumentando {aum}%, temos R${aumentar(valor, aum)}')
print(f'Diminuindo {dim}%, temos R${diminuir(valor, dim)}')