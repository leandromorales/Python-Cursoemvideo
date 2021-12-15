#Faça um programa que leia um ano qualquer e mostre se ele é Bissexto.

ano = int(input('Digite um ano: '))
bis = ano % 4
biss = ano % 100
bisse = ano % 400

if bis == 0:
    if biss == 0 and bisse == 0:
            print('O ano {} é bissexto.')
    else:
        print('O ano {} não é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))


#print(bis)
#print(biss)
#print(bisse)

#https://docs.microsoft.com/pt-br/office/troubleshoot/excel/determine-a-leap-year#:~:text=Qualquer%20ano%20que%20seja%20uniformemente,e%201996%20s%C3%A3o%20anos%20bissextos.