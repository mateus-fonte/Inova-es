def contador(inicio, fim, passo):
    import time
    print('-='*30)
    print(f'Contagem de {inicio} a {fim} de {abs(passo)} em {abs(passo)} ')
    for n in range(inicio, fim+1 if passo >= 0 else fim - 1, passo):
        print(n, end=' ')
        time.sleep(0.5)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, -2)
print('Agora é sua vez de personalizar a contagem!')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
