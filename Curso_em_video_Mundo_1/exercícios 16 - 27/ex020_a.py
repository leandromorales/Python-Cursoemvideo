
from random import shuffle
cont = 1
ap = list()
while cont <=4:
    ap.append(input('Digite o nome da {}ª pessoa: '.format(cont)))
    cont = cont + 1
shuffle(ap)
print('A ordem de apresentação aleatória será: \n# {}\n## {}\n### {}\n#### {}'.format(ap[0], ap[1], ap[2], ap[3]))