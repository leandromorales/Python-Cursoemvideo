'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.

'''

produtos = ('Lápis', 2.50, 'Caneta', 3.00, 'Lapiseira', 4.50, 'Caderno', 22.00, 'Borracha', 0.75)

#print(produtos)
print('-' * 40)
print(f'{"Lista de preços":^40}')
print('-' * 40)
for n in range(0, len(produtos)):
    if n % 2 == 0:
        print(f'{produtos[n]:.<30}', end=' ')
    else:
        print(f'R${produtos[n]:>6.2f}')
print('-' * 40)