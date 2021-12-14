#Faça um programa que leia um ano qualquer e mostre se ele é Bissexto.

ano = int(input('Digite um ano: '))
bis = ano % 4
biss = ano % 100
bisse = ano % 400

if bis == 0:
    if biss == 0:
        if bisse == 0:
            print('O ano {} é bissexto')
print(bis)
print(biss)
print(bisse)