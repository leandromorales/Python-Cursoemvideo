#A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
# sua categora, de acordo com a idade:
# - Até 9 anos: Mirim;
# - Até 14 anos: Infantil;
# - Até 19 anos: Junior;
# - Até 25 anos: Sênior
# - Acima: Master

from datetime import date
ano = date.today().year
nasc = int(input('Digite o seu ano de nascimento: '))
idade = ano - nasc
p1 = 'O atleta tem'
p2 = 'ano de idade e pertence à categoria'
p3 = 'anos de idade e pertence à categoria'

if idade <= 0:
    print('{} menos de um {} Mirim.'.format(p1, p2))
elif idade == 1:
    print('{} {} {} Mirim.'.format(p1, idade, p2))
elif idade <= 9:
    print('{} {} {} Infantil.'.format(p1, idade, p3))
elif idade <= 14:
    print('{} {} {} Infantil.'.format(p1, idade, p3))
elif idade <= 19:
    print('{} {} [} Júnior.'.format(p1, idade, p3))
elif idade <= 25:
    print('{} {} {} Sênior.'.format(p1, idade, p3))
else:
    print('{} {} {} Master.'.format(p1, idade, p3))