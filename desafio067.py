while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 35)
    cont = 1
    tab = cont * n
    if n < 0:
        break
    while cont <= 10:
        tab = cont * n
        print(f'{n} x {cont} = {tab}')
        cont += 1
    print('-' * 35)



