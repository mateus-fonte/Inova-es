print('-'*25)
print('Sequência de Fibonacci')
print('-'*25)
x = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('{} » {}'.format(t1, t2), end='')
cont = 3
while cont <= x:
    t3 = t2 + t1
    print(' » {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' FIM')






