#Escreva um programa que pergunte a quantidade de quilômetros percorridos por um carro alugardo
#e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
# custa R$60 por dia e R$0,15 por km rodado.

dias = int(input('Digite quantos dias o carro foi alugado: '))
km = float(input('Digite quantos quilômetros foram rodados: '))
totald = dias * 60
totalkm = km * 0.15
valor = totalkm + totald
print('O valor total da locação por {:.0f} dias e {:.2f} KM foi de R${:.2f}!'.format(dias, km, valor))