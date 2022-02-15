r1 = float(input('Digite o comprimento do primeiro segmento de reta:'))
r2 = float(input('Digite o comprimento do segundo segmento de reta:'))
r3 = float(input('Digite o comprimento do terceiro segmento de reta:'))
if r1 + r3 > r2 and r2 + r3 > r1 and r1 + r2 > r3:
    print('O tringulo formado por {}, {} e {} é possivel'.format(r1, r2, r3))
else:
    print('Os segmentos de reta {}, {} e {} não formam um triangulo'.format(r1, r2, r3))
