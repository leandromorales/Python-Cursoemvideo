# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Informe seu sexo: ')).strip().upper()[0]
while sexo not in 'MmFm':
    sexo = str(input('Dados inválidos. Por favor, Informe seu sexo: ')).strip().upper()[0]
print('Sexo {} resgistrado com sucesso.'.format(sexo))