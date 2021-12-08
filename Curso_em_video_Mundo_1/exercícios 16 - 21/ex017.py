#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
#calcule e mostre o comprimento da hipotenusa.
from math import hypot
#import math

op = float(input('Digite a medida do cateto oposto: '))
ad = float(input('Digite a medida do cateto adjacente: '))
#hyp = (op ** 2 + ad ** 2) ** (1/2)
#hyp = math.hypot(op, ad)
hyp = hypot(op, ad)
print('Para o cateto oposto de {} e cateto adjacente de {}, o valor da Hypotenusa é {:.2f}'.format(op, ad, hyp))