#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A";
#Em que posição ela aparece a primeira vez;
#Em que posição ela aparece a última vez:

frase = str(input('Digite uma frase: ')).strip().upper()
#frase = frase.upper()
print('A letra "A" aparece: {}'.format(frase.count('A')))
print('A primeira posição {}'.format(frase.find('A')+1))
print('A última posição {}'.format(frase.rfind('A')+1))




#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
#e o segundo nome separadamente.
#Primeiro nome:
#Segundo nome:

#nome = str(input('Digite seu nome: '))
#nome = nome.split()
#print('O primeiro nome é: {} e o segundo nome é: {}.'.format(nome[0], nome[1]))