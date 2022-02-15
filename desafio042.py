r1 = float(input('Digite o comprimento do 1º segmento de reta:'))
r2 = float(input('Digite o comprimento do 2º segmento de reta:'))
r3 = float(input('Digite o comprimento do 3º segmento de reta:'))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Os segmento de reta podem formar um triângulo, ', end='')
    if r1 != r2 and r1 != r3 and r2 != r3:
        print('O triângulo formado é escaleno')
    if r1 == r2 and r1 != r3 or r2 == r3 and r2 != r1 or r1 == r3 and r3 != r2:
        print('O triângulo formado é isósceles')
    if r1 == r2 == r3:
        print('O triângulo formado é equilátero')
else:
    print('Os segmentos de reta não formam um triângulo')
