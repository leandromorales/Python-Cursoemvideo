
###Exemplos de fatiamento:
frase = str('Curso em Vídeo Python')

print(frase[9])
print(frase[9:14])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

###Exemplos de análise:

#Número de caracteres
print(len(frase))

#Contar quantas vezes o caracter existe na str
print(frase.count('o'))

#Procurar caracteres e mostrar posição de início
print(frase.find('deo'))

#Quando o valor procurado não existe (exibe o valor -1)
print(frase.find('Leandro'))

#Existe a palavra dentro da string?
print('Curso' in frase)

###Exemplos de transformação:

#Substituir caracteres
frase2 = frase.replace('Python','Java')
print (frase2)

#Método Upper
frase3 = frase.upper()
print(frase3)

#Método Lower
frase4 = frase.lower()
print(frase4)

#Método Capitalize
frase5 = frase.capitalize()
print(frase5)

#Método Title
frase6 = frase.title()
print(frase6)

#Método Strip
frase100 = str('   Aprenda Python  ')

frase101 = frase100.strip()
print(frase101)

#Método Rstrip
frase102 = frase100.rstrip()
print(frase102)

#Método Lstrip
frase103 = frase.lstrip()
print(frase103)

#Método split
frase7 = frase.split()
print(frase7)

#Método join
frase8 = '-'.join(frase7)
print(frase8)
