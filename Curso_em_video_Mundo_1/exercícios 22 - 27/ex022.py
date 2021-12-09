#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas;
#O nome com todas as letras minúsculas;
#Quantas letras tem no nome (sem considerar os espaços);
#Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo:'))
#nomec = nome.replace(' ','')
#print(nomec)

print('''O seu nome em letras maiúsculas é: {}
O seu nome com letras minúsculas é: {}
O seu nome completo tem {} letras
O seu primeiro nome tem {} letras '''.format(nome.upper(), nome.lower(), len(nome.replace(' ', '')), len(nome.split()[0])))

