print('{:»^40}'.format(' LOJAS DAF '))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista cheque/dinheiro
[ 2 ] à vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção =int(input('Sua opção: '))
if opção == 1:
    valor = preço - 10*preço/100
    print(f'O valor final a ser pago é R${valor} com R${preço-valor} de desconto ')
elif opção == 2:
    valor = preço - 5*preço/100
    print(f'O valor final a ser pago é R${valor} com R${preço-valor} de desconto ')
elif opção == 3:
    valor = preço
    print(f'O valor final a ser pago é R${valor} ')
elif opção == 4:
    parcelas = int(input('Em quantas parcelas você deseja pagar?'))
    valor = preço + 20*preço/100
    print(f'Sua compra sera parcelada em {parcelas}x de R${valor/parcelas} COM JUROS')
    print(f'O valor final a ser pago é R${valor} com R${valor-preço} de juros')
else:
    print('ERRO, digite o código novamente')



