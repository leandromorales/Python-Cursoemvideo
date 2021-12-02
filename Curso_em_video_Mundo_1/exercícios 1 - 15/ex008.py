#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
metro=float(input('Digite um valor em metros: '))
cent=metro*100
mili=metro*1000
print('A medida de {} metros é igual a {} centímetros e {} milímetros.'.format(metro, cent, mili))