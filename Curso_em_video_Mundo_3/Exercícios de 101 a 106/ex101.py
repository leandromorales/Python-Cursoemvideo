'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
nascimento da pessoa, retornando um valor literal indicando se a pessoa tem voto NEGADO, OPCIONAL
ou OBRIGATÓRIO nas eleições.'''

def voto(nasc):
    from datetime import date
    ano = date.today().year
    idade = ano - nasc
    if idade >= 16 and idade <18 or idade > 65:
        votar = 'OPCIONAL'
    elif idade >= 18 and idade < 65:
        votar = 'OBRIGATÓRIO'
    else:
        votar = 'NEGADO'
    return (f'Com a idade de {idade} anos o voto é {votar}.')



#Código principal

print(voto((int(input('Digite o ano de nascimento: ')))))