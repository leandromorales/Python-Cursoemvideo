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

if idade <= 0:
    print('O atleta ainda não tem um ano de idade e está na categoria Mirim.')
elif idade == 1:
    print('O atleta tem {} ano de idade e está na categoria Mirim. '.format(idade))
elif idade > 1 and idade <= 9:
    print('O atleta tem {} anos de idade e está na categoria Mirim. '.format(idade))
elif idade > 9 and idade <= 14:
    print('O atleta tem {} anos de idade e está na categoria Infantil. '.format(idade))
elif idade > 14 and idade <= 19:
    print('O atleta tem {} anos de idade e está na categoria Junior. '.format(idade))
elif idade > 19 and idade <= 25:
    print('O atleta tem {} anos de idade e está na categoria Sênior. '.format(idade))

else:
    print('O atleta {} anos de idade e está na categoria Master. '.format(idade))


