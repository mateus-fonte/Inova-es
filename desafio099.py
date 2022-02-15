def maior(*valores):
    import time
    m = 0
    print('-='*30)
    print('Analisando os valores passados...')
    for c in range(0, len(valores)):
        if c == 0:
            m = c
        if c > m:
            m = c
        print(c, end=' ')
        time.sleep(0.3)
    print(f'Foram informados {len(valores)} ao todo.')
    print(f'O maior valor informado foi o {m}')


maior(7, 3, 2, 9, 11, 12)
maior(2, 3, 4, 5)
maior()

