#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco=float(input('Digite o preço do produto: '))
calc=(preco*5)/100
final=preco-calc
print('O preço original do produto é R${}, com desconto de 5% fica R${:.2f}'.format(preco, final))
