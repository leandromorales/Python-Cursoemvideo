#Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais;
# - Isósceles: dois lados iguais;
# - Escaleno: todos os lados diferentes.
l1 = float(input('Digite o comprimento da primeira reta: '))
l2 = float(input('Digite o comprimento da segunda reta: '))
l3 = float(input('Digite o comprimento da terceira reta: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    if l1 == l2 == l3:
        print('As retas formam um triângulo equilátero.')
    elif l1 != l2 != l3 != l1:
        print('As retas formam um triângulo escaleno.')
    else:
        print('As retas formam um triângulo isósceles.')

else:
    print('As retas não formam um triângulo.')