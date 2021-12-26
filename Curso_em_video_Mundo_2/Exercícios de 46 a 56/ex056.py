# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
# - A média de idade do grupo;
# - Qual é o nome do homem mais velho;
# - Quantas mulheres têm menos de 20 anos.

nomemaior = ''
idademaior = 0
soma = 0
cont = 0
for c in range(1, 5):
    nome = str(input('Digite o nome da pessoa: '))
    idade = int(input('Digite a idade da pessoa: '))
    sexo = int(input('''Sexo (M1/F2): '''))
    soma += idade
    if sexo == 1:
        if c == 1:
            nomemaior = nome
            idademaior = idade
        else:
            if idade > idademaior:
                nomemaior = nome
                idademaior = idade

    if sexo == 2 and idade < 20:
        cont += 1

print('O homem mais velho tem {} anos de idade.'.format(nomemaior))
print('{} mulheres têm menos de 20 anos de idade.'.format(cont))
print('A média de idade do grupo é {} anos.'.format(soma/4))
