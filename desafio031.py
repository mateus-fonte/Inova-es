v = float(input('Digite a distancia da viagem em kms:'))
if v <= 200:
    p = v * 0.5
    print('O valor da viagem é {} reais'.format(p))
else:
    p = v * 0.45
    print('O valor da viagem é {} reais'.format(p))
print('Boa viagem!')
