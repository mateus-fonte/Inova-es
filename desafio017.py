from math import hypot
a = float(input('Qual o comprimento do primeiro cateto?'))
b = float(input('E do segundo?'))
h = hypot(a, b)
print('a hipotenusa formada por esses dois catetos é {:.2f}'.format(h))
