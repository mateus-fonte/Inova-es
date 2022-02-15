num = int(input('Digite um número para calcular seu fatorial: '))
f = 1
c = num
print('Calculando o fatorial de {}! = '.format(num), end='')
while c > 0:
    print('{} x '.format(c) if c > 1 else '{} = '.format(c), end='')
    f *= c
    c -= 1
print('{}'.format(f))
