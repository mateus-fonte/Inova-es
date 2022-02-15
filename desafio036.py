v = float(input('Qual o valor do imovél?'))
s = float(input('Qual o salário do comprador em reais?'))
a = int(input('Em quantos anos ele pretende pagar?'))
p = v/(a*12)
if p > 30*s/100:
    print('Infelizmente o imovél não poderá ser financiado')
else:
    print('Parabéns! seu financiamento foi aprovado e o valor da parcela mensal será de {} reais'.format(p))
