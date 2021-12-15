#Desenvolva um programa que pergunte a distância de uma viagem em km.
#Calcule o preço da passagem, cobrando R$0,50 por km até 200km e R$0,45 para viagens mais longas.

distancia = float(input('Digite a distância da sua viagem: '))

preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O preço da sua passagem é R${:.2f}.'.format(preco))