n = int(input('Digite um número: '))
tot = 0
for c in range(1, n+1):
    if n % c == 0:
        tot += 1
        print('\33[33m', end='')
    else:
        print('\33[31m', end='')
    print('{} '.format(c), end='')
print('\n\33[mO número {} foi divisível {} vezes'.format(n, tot))
if tot == 2:
    print('\33[32mPor isso ele é PRIMO!')
else:
    print('\33[37mPor isso ele NÃO É PRIMO!')
