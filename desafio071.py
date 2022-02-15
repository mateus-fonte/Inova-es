print('='*30)
print('{:^30}'.format('BANCO DAFINANÇAS'))
print('='*30)
dinheiro = int(input('Quantos reais você deseja sacar? R$'))
quantia = dinheiro
ced = 50
totced = 0
while True:
    if quantia >= ced:
        totced += 1
        quantia -= ced
    else:
        print(f'Total de {totced} cédulas de {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if quantia == 0:
            break