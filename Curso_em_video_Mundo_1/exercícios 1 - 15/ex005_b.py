#Desafio N5: Faça um programa que leia um número e mostre o seu sucessor e seu antecessor

num = int(input('Digite um número: '))
print('O antecessor de {} é {}. O sucessor de {} é {}'.format(num, (num-1), num, (num+1)))