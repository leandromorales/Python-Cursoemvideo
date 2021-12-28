# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.


sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()
while sexo != 'M' and sexo!= 'F':
    print('Dados inválidos, tente novamente.')
    sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()
print('O sexo da pessoa é {}.'.format(sexo))