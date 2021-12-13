#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas;
#O nome com todas as letras minúsculas;
#Quantas letras tem no nome (sem considerar os espaços);
#Quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome completo: ')).strip()
print('''O seu nome em letras maiúsculas é: {};
O seu nome em letras minúsculas é: {}; 
Seu nome tem {} letras;
Seu primeiro nome tem {} letras.
'''.format(nome.upper(), nome.lower(), len(nome) - nome.count(' '), len(nome.split()[0])))