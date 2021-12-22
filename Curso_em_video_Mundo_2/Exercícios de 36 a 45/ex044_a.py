# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À vista Dinheiro/Cheque: 10% de desconto;
# - À vista no cartão: 5% de desconto;
# - Em até 2x no cartão: preço normal;
# - 3x ou mais no cartão: 20% de juros.

print('{:=^40}'.format('lojas Guanabara'))
preço = float(input('Preço das compras: R$ '))
print('''Digite o número correspondente à condição de pagamento:
    [ 1 ] 10% de desconto à vista no Dinheiro/Cheque;
    [ 2 ] 5% de desconto à vista no cartão;
    [ 3 ] 2x no cartão;
    [ 4 ] 3x com juros de 20%.
    Sua opção: ''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparcela = int(input('Quantas parcelas? '))
    parcela = total / totparcela
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(totparcela, parcela))
else:
    total = preço
    print('Opção inválida de pagamento. Tente novamente. ')

print('A sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))