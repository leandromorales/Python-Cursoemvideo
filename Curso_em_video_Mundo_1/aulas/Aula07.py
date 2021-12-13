#Ordem de precedência:
#1: ()
#2: **
#3: * / // %
#4: + -

o1 = float(5+2)
o2 = float(5-2)
o3 = float(5*2)
o4 = float(5/2)
o5 = float(5**2)
o6 = int(5 // 2)
o7 = int(5 % 2)

print("5 + 2 = {}".format(o1))
print('5 - 2 = {}'.format(o2))
print('5 x 2 = {}'.format(o3))
print('5 / 2 = {}'.format(o4))
print('5 elevado a 2 = {}'.format(o5))
print('5 // 2 ='.format(o6))
print('O resto da divisão de 5 / 2 é ='.format(o7))

aa = int(3*(5+4)**2)
print('AA ígual a: {}'.format(aa))