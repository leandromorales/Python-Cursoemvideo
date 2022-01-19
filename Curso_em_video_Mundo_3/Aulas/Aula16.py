lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim'
print(lanche)
print(lanche[1])
print(lanche[1:])
print(lanche[-2])
print(lanche[-3:])
print(len(lanche))


#Laço de repetição com tupla:
for cont in lanche:
    print(f'Eu vou comer {cont}')
print('Comi para caramba.')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('Comi para caramba.')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

#Organizar os itens de uma tupla:
print(sorted(lanche))

#As Tuplas são imutáveis durante a execução do programa.

#Concatenar Tuplas
a = (2, 3, 4)
b = (6, 0, 7, 3)
c = b + a
print(c)
#Contar a ocorrência de elementos:
print(c.count(0))

#Tuplas comportam mais de um tipo de dado:

pessoa = (28, 'Gustavo', 55.98)
print(pessoa)

#Apagar tupla

del(pessoa)