#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.
salario=float(input('Digite o salário do funcionário: '))
aumt=(salario*11.9)/100
final=salario+aumt
print('O salário do funcionario era R${:.2f}. Com o aumento de 15% foi para R${:.2f}.'.format(salario, final))