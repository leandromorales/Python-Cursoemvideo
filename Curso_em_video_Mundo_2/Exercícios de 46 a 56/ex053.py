#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
#Ex: APOS A SOPA
#A sacada da casa
#a torre da derrota
#o lobo ama bolo
#Anotaram a data da maratona

frase = str(input('Digite uma frase: ')).strip()

#print(frase)

#remover os espaços:

frase2 = frase.replace(' ', '')
frase3 = frase2

#print(frase2)

#comparar caracteres

for c in range(0, len(frase2)):
    print(frase2[c], end='-')
    print(c, end=' ')

print('\n')
for d in range(len(frase2) - 1, -1, -1):
    print(frase2[d], end='-')
    print(d, end=' ')


#for c in range(0, len(frase)):
#    #print(c)
#    if frase[c] == ' ':
#        frase2 = frase.replace(' ', '')

