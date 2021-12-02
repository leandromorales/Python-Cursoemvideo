#Desafio N5: Faça um programa que leia um número e mostre o seu sucessor e seu antecessor
control = False
cont = 0
while control == False and cont <3:
    cont = cont+1
    num = input('Digite um número: ')
    num_test = num.isnumeric()
    if num_test:
        control = True
        num = int(num)
        #print(control)

#print('O valor digitado é: ', type(num))
num_ant = num-1
num_suc = num+1
print('O antecessor de {} é {}.\nO sucessor de {} é {}.'.format(num, num_ant, num, num_suc))

