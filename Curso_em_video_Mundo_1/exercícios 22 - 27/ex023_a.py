#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
#Unidade
#Centena
#Dezena
#Milhar

num = -1
cont = 4

while (num < 0 or num > 9999) and cont >= 1:
    num = int(input('Digite um número de 0 a 9999: '))
    cont = cont - 1
    if cont == 1:
        print('Você tem mais {} tentativa! '.format(cont))
    else:
        print('Você tem mais {} tentativas! '.format(cont))
    if cont == 0:
        print('O programa será encerrado.')
        break

num = str(num)

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
