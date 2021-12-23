#Refaça o desafio 009, mostrando uma tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

num = int(input('Digite um número para ver sua tabuada: '))
for x in range(1, 11):
    print('{} X {} = {}'. format(num, x, num*x))