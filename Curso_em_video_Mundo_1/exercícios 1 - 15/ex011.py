#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
#e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

alt=float(input('Digite a altura da parede em M: '))
larg=float(input('Digite a largura da parede em M: '))

area=alt*larg
litro=2
tinta=area/litro
print('A parede tem {:.2f}M². Serão necessários {:.2f}L de tinta para pintá-la.'.format(area, tinta))