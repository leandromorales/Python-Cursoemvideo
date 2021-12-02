#Faça um programa que leia um número inteiro e mostre na tela a sua tabuada.
num=int(input('Digite um número inteiro: '))

cont=1
print('-'*12)
while cont<=10:
    num1=num*cont
    print('{} X {:2} ={}'.format(num, cont, num1))
    cont=cont+1
print('-'*12)