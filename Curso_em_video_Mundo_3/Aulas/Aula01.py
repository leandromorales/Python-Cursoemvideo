lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim'
print(lanche)
print(lanche[1])
print(lanche[1:])
print(lanche[-2])
print(lanche[-3:])
print(len(lanche))



for cont in lanche:
    print(f'Eu vou comer {cont}')
print('Comi para caramba.')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('Comi para caramba.')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')



#As Tuplas são imutáveis durante a execução do programa.

