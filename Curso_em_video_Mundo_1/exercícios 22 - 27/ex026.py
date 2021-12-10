#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
#e o segundo nome separadamente.
#Primeiro nome:
#Segundo nome:

nome = str(input('Digite seu nome: '))
nome = nome.split()
print('O primeiro nome é: {} e o segundo nome é: {}.'.format(nome[0], nome[1]))