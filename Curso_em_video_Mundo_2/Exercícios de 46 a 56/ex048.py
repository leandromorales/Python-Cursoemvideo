#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de
# três e que se encontram no intervalo de 1 até 500.
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont = cont + 1

print('A soma dos {} valores solicitados é igual a: {}.'.format(cont, soma))
#print(soma)
#print(cont)