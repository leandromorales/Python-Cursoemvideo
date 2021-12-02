#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares
#ela pode comprar. Considere U$$1,00 = R$3,27

#cur=int(input('Digite o valor em R$:'))
cur=float(input('Digite o valor em R$:'))
exch=3.27
calc=cur/exch
print('Com R${:.2f} você pode comprar U$${:.2f}.'.format(cur, calc))