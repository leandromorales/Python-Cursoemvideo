#Refaça o desafio 009, mostrando uma tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.
print('-'* 20)
num = int(input('Digite um número para saber a sua tabuada: '))

for c in range(1, 11):
    num1 = num * c
    print('{} X {} = {}'.format(num, c, num1))
print('-' * 20)