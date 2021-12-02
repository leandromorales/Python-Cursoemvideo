#Escreva um programa que converta uma temperatura digitada em C para F.
# fah = cel * 1.8 + 32

cel = float(input('Digite a temperatura em ºC: '))
fah = cel * 1.8 + 32
print('A temperatura {:.2f}ºC é igual a {:.2f}ºF!'.format(cel,fah))