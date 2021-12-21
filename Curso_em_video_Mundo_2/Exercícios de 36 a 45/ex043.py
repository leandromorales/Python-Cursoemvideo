#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o seu IMC e mostre seu status, de acordo com
#a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso;
# - Entre 18.5 e 25: Peso ideal;
# - Entre 25 até 30: Sobrepeso;
# - Entre 30 até 40: Obesidade;
# - Acima de 40: Obesidade mórbida.

peso = float(input('Digite o seu peso em KG: '))
altura = float(input('Digite a sua altura: '))
imc = peso / altura ** 2
#print(imc)

m1 = 'O seu IMC é de'
m2 = 'e você está com'
if imc < 18.5:
    print('{} {:.1f} e você está abaixo do peso.'.format(m1, imc))
elif imc <= 25:
    print('{} {:.1f} {} peso normal.'.format(m1, imc, m2))
elif imc <= 30:
    print('{} {:.1f} {} sobrepeso.'.format(m1, imc, m2))
elif imc <= 40:
    print('{} {:.1f} {} obesidade.'.format(m1, imc, m2))
else:
    print('{} {:.1f} {} obesidade mórbida'.format(m1, imc, m2))