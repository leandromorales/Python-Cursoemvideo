# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A - Quantas pessoas tem mais de 18 anos;
# B - Quantos homens foram cadastrados;
# C - Quantas mulheres tem menos de 20 anos.

maiores = 0
homens = 0
mulheres20 = 0
print('=' * 30)
while True:
    idade = int(input('Digite a idade pessoa: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    if idade > 18:
        maiores += 1
    if sexo in 'M':
        homens += 1
    if sexo in 'F' and idade < 20:
        mulheres20 += 1
    conti = ' '
    while conti not in 'SN':
        conti = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if conti in 'N':
        break
    print('=' * 30)

print('=' * 30)

if maiores == 0:
    print('Nenhuma pessoa informada é maior de 18 anos.')
elif maiores == 1:
    print(f'Foi informada 1 pessoa maior de 18 anos.')
else:
    print(f'Foram informadas {maiores} pessoas maiores de 18 anos.')

if homens == 0:
    print('Não foi informado nenhum homem.')
elif homens == 1:
    print('Foi informado 1 homem.')
else:
    print(f'Foram informados {homens} homens.')


if mulheres20 == 0:
    print('Não foi informada nenhuma mulher menor de 20 anos.')
elif mulheres20 == 1:
    print(f'Foi informada 1 mulher menor de 20 anos.')
else:
    print(f'Foram informadas {mulheres20} mulheres menores de 20 anos')



