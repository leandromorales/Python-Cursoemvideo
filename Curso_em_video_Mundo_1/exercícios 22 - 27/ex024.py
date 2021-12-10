#Crie um programa que leia o nome de uma cidade e diga se ela começa com o nome "SANTO"

cid = str(input('Digite o nome de uma cidade: '))
cidupp = cid.upper()
cidspl = cidupp.split()
cidfinal = cidspl[0]


if ('SANTO' in cidfinal):
    print('O nome da cidade começa com a palavra "Santo".')
else:
    print('O nome da cidade não começa com a palavra "Santo".')

