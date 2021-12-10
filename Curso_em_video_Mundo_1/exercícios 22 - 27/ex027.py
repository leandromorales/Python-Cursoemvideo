#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
#e o último nome separadamente:
#Primeiro nome:
#Último nome:

nome = str(input('Digite seu nome: '))
nome = nome.split()
cont = len(nome)
#print(nomelen)
last = cont - 1
print('O primeiro nome é: {} e o último nome é: {}.'.format(nome[0], nome[last]))