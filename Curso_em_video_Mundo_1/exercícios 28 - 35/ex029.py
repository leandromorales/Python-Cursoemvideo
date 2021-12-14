#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80KM/H, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada km acima do limite.

vel = float(input('Digite a velocidade do carro em KM/H: '))
if vel > 80:
    print('Você foi multado.')
    calc = vel - 80
    multa = calc * 7
    print('Você excedeu a velocidade máxima em: {}KM/H e será multado em R${}.'.format(calc, multa))
else:
    print('Você não foi multado.')