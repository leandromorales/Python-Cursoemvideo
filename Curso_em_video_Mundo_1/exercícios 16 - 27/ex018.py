#Faça um programa que leia um ângulo qualquer e mostre na tela o valor de seno, coseno e tangente
from math import radians, sin, cos, tan
#import math
ang = float(input('Digite um ângulo: '))
ang = radians(ang)
sen = sin(ang)
cos = cos(ang)
tan = tan(ang)
print('Para o ângulo de {}º, temos os seguintes valores: \nSeno {:.2f}\nCoseno {:.2f}\nTangente {:.2f}.'.format(ang, sen, cos, tan))