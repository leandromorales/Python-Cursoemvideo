#Desafio N5: Faça um programa que leia um número e mostre o seu sucessor e seu antecessor

num = int(input('Digite um número: '))
num_ant = num-1
num_suc = num+1
print('O antecessor de {} é {} e o sucessor de {} é {}.'.format(num, num_ant, num, num_suc))
