s = float(input('Digite seu salário:'))
if s > 1250.00:
    print('O seu novo salário é {} reais'.format(s+(10*s/100)))
else:
    print('O seu novo salário é {} reais'.format(s+15*s/100))
