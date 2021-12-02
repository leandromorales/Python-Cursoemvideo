t1 = input('Digite algo: ')

print('O tipo primitivo desse valor é: ', type(t1))
print('Só tem letras? ', t1.isalpha())
print('Só tem números? ', t1.isnumeric())
print('Sò tem espaços? ', t1.isspace())
print('Somente maiúsculas? ', t1.isupper())
print('Somente minúsculas?', t1.islower())
print('Está capitalizada?', t1.istitle())
