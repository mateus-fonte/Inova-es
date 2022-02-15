v = float(input('Digite a velocidade do carro em km/h:'))
if v >= 80:
    x = v - 80
    print('Você ultrapassou o limite de velocidade permitida e terá que pagar {:.1f}'.format(7*x))
