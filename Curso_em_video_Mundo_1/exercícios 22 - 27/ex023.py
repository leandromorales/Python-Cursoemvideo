#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
#Unidade
#Centena
#Dezena
#Milhar

num = str(input('Digite um número de 0 a 9999: '))

if len(num) == 1:
    #print('1')
    print('Unidade: {}'.format(num[0]))
elif len(num) == 2:
    #print('2')
    print('''Unidade: {}\nDezena: {}'''.format(num[1], num[0]))
elif len(num) == 3:
    #print('3')
    print('''Unidade: {}\nDezena: {}\nCentena: {}'''.format(num[2], num[1], num[0]))
elif len(num) == 4:
    #print('4')
    print('''Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'''.format(num[3], num[2], num[1], num[0]))
