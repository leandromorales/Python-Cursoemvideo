#Escreva um programa que pergunte o salário de um funcionário e calcule o valor
# de seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Digite o seu salário: '))

if sal > 1250.00:
    calc = (sal * 10) / 100
    print('''O aumento de salário de 10% será de R${:.2f}, 
    o valor final será R$ {:.2f}'''.format(calc, sal +calc))
else:
    calc = (sal * 15) / 100
    print('''O aumento de salário de 15% será de R${:.2f},
    o valor final será R${:.2f}.'''.format(calc, sal + calc))