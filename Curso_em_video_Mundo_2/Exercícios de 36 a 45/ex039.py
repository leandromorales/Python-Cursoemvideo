#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar;
# - Se é a hora de se alistar;
# - Se já passou o tempo do alistamento;
# Seu programa também deve mostrar quanto tempo que falta ou que passou do prazo.

#    ano = date.today().year
from datetime import date

nasc = int(input('Digite o ano de seu nascimento: '))
ano = date.today().year
#ano = 2017
idade = ano - nasc
print('Você tem {} anos de idade em {}.'.format(idade, ano))

if idade < 18:
    print('Você ainda vai se alistar no serviço militar.')
    dif = 18 - idade
    if dif == 1:
        print('Falta 1 ano para você se alistar.'.format(dif))
    else:
        print('Faltam {} anos para você se alistar.'.format(dif))

elif idade == 18:
    print('Você deve se alistar imediatamente.')

else:
    dif = idade - 18
    if dif == 1:
        print('Você excedeu o prazo de alistamento em 1 ano.')
    else:
        print('Você excedeu o prazo de alistamento em {} anos.'.format(dif))