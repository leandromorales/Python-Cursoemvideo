#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

nome = str(input('Digite seu nome completo: '))
nome = nome.upper()

if ('SILVA' in nome):
    print('Seu nome contém a palavra "Silva".')
else:
    print('Seu nome não contém a palavra "Silva".')

