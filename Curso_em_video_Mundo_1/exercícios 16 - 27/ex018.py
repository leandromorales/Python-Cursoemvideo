#Faça um programa que leia um ângulo qualquer e mostre na tela o valor de seno, coseno e tangente
import math
ang = float(input('Digite um ângulo: '))
sen = math.sin(ang)
cos = math.cos(ang)
tan = math.tan(ang)
print('Para o ângulo de {}º, temos os seguintes valores: \nSeno {:.2f}\nCoseno {:.2f}\nTangente {:.2f}.'.format(ang, sen, cos, tan))