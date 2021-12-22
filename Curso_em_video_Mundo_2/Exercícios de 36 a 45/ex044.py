# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À vista Dinheiro/Cheque: 10% de desconto;
# - À vista no cartão: 5% de desconto;
# - Em até 2x no cartão: preço normal;
# - 3x ou mais no cartão: 20% de juros.

def calculo():
    #print(condicao)
    if condicao == 1:
        desconto = (preco * 10)/100
        final = preco - desconto
        print('Opção à vista Dinheiro/Cheque escolhida.')
        print('Valor final da compra: R${}'.format(final))
    elif condicao == 2:
        desconto = (preco * 5)/100
        final = preco - desconto
        print('Opção à vista no Cartão escolhida.')
        print('Valor final da compra: R${}'.format(final))
    elif condicao == 3:
        print('Opção normal de pagamento, em até 2x.')
        print('Valor final da compra: R${}'.format(preco))
    else:
        juros = (preco * 20) / 100
        final = preco + juros
        print('Opção parcelada em até 3x, com acréscimo de 20%.')
        print('Valor final da compra R${}'.format(final))

preco = float(input('Digite o valor do produto: R$ '))

contador = 4
condicao = 2
while contador > 0:
    condicao = int(input('''Digite o número correspondente à condição de pagamento:
    [ 1 ] 10% de desconto à vista no Dinheiro/Cheque;
    [ 2 ] 5% de desconto à vista no cartão;
    [ 3 ] 2x no cartão;
    [ 4 ] 3x com juros de 20%.
    Sua opção: '''))
    if condicao >= 1 and condicao <= 4:
        calculo()
        contador = 0
    else:
        contador = contador - 1
        if contador == 1:
            print('Opção incorreta. Você tem mais uma tentativa.')
        elif contador == 0:
            print('0 programa será encerrado.')
        else:
            print('Opção incorreta. Você tem {} tentativas.'.format(contador))

#print('Condição')