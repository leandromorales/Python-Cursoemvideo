#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será
#negado.


valor = float(input('Digite o valor da casa que você quer comprar: R$'))
salario = float(input('Digite o seu salário atual: R$'))
anos = float(input('Digite em quantos anos você que pagar o financiamento: '))

presta = valor / (anos*12)
#porcentagem = (salario * 30) / 100

if presta > (salario * 30 ) / 100:
    print('''O financiamento não foi aprovado. 
    A prestação no valor de "R${:.2f}" excede o limite de 30% do salário.'''.format(presta))
else:
    print('O financiamento foi aprovado e a prestação será no valor de "R${:.2f}"'.format(presta))

