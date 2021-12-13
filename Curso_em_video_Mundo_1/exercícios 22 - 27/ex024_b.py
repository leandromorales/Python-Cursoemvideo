#Crie um programa que leia o nome de uma cidade e diga se ela começa com o nome "SANTO"

cid = str(input('Digite a cidade em que você nasceu: ')).strip()
print(cid[0:5].upper() == 'SANTO')
