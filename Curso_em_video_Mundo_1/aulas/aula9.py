
###Exemplos de fatiamento:
frase = str('Curso em Vídeo Python')
print('Frase original 1: "{}"'.format(frase))
print('Caractere posição 9: "{}"'.format(frase[9]))
print('Caracteres da posição 9 até a posição 14: "{}"'.format(frase[9:14]))
print('Caracteres da posição 9 até a posição 21, pulando de dois em dois caracteres: "{}"'.format(frase[9:21:2]))
print('Carateres do início até a posição 5: "{}"'.format(frase[:5]))
print('Caracteres da posição 15 até o final: "{}"'.format(frase[15:]))
print('Caracteres da posição 9 até o final, pulando de 3 em 3 caracteres: "{}"'.format(frase[9::3]))

###Exemplos de análise:

#Número de caracteres
print('Quantidade de caracteres da frase: "{}"'.format(len(frase)))

#Contar quantas vezes o caracter existe na str
print('Quantidade de vezes que o caracter "o" aparece na frase: "{}"'.format(frase.count('o')))

#Procurar caracteres e mostrar posição de início
print('Posição inicial que os caracteres "deo" aparecem na frase: "{}"'.format(frase.find('deo')))

#Quando o valor procurado não existe (exibe o valor -1)
print('Procura de valor na frase. Caso o valor não exista, será exibido: "{}"'.format(frase.find('Leandro')))

#Existe a palavra dentro da string?
print('Teste lógico se existe a expressão na variável: "{}"'.format('Curso' in frase))

###Exemplos de transformação:

#Substituir caracteres
frase2 = frase.replace('Python','Java')
print('Substituição de caracteres: "{}"'.format(frase2))

#Método Upper
frase3 = frase.upper()
print('"Upper", transforma todos os caracteres em maiúsculos: "{}"'.format(frase3))

#Método Lower
frase4 = frase.lower()
print('"Lower", transforma todos os caracteres em minúsculos: "{}"'.format(frase4))

#Método Capitalize
frase5 = frase.capitalize()
print('"Capitalize", transforma o primeiro caracter da string em maiúscula: "{}"'.format(frase5))

#Método Title
frase6 = frase.title()
print('"Title", transforma a primeira letra de todas as palavras da string em maiúscula: "{}"'.format(frase6))

#Método Strip
frase100 = str('   Aprenda Python  ')
print('Frase com espaços antes e depois das palavras: "{}"'.format(frase100))

frase101 = frase100.strip()
print('"Strip", remove os espaços em branco no início e final da string: "{}"'.format(frase101))

#Método Rstrip
frase102 = frase100.rstrip()
print('"rstrip", remove os espaços à direita da string: "{}"'.format(frase102))

#Método Lstrip
frase103 = frase100.lstrip()
print('"lstrip", remove os espaços à esquerda da string: "{}"'.format(frase103))

#Método split
frase7 = frase.split()
print('"Split", separa a string de acordo com o caracter escolhido como separador, \nneste caso o espaço: "{}"'.format(frase7))

#Método join
frase8 = '-'.join(frase7)
print('"join", une os elementos de uma lista com o separador escolhido: "{}"'.format(frase8))
