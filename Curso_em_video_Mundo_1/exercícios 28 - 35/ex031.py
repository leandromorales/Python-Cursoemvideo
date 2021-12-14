#Desenvolva um programa que pergunte a distância de uma viagem em km.
#Calcule o preço da passagem, cobrando R$0,50 por km até 200km e R$0,45 para viagens mais longas.

dis = float(input('Digite a distância da viagem em KM: '))

if dis <= 200:
    #print('50c')
    passagem = dis * 0.50
else:
    #print('45c')
    passagem = dis * 0.45

print('O preço da passagem é: R${:.2f}'.format(passagem))