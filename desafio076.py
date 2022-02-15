lista = ('banana', 1.50, 'maçã', 2.00, 'arroz', 1.80, 'feijão', 2.00, 'mel', 4.00, 'atum', 0.80, 'uva', 2.60, 'tangerina', 2.00)
print('=-'*20)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('=-'*20)
for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<30}', end='')
    else:
        print(f'R${lista[c]:>5.2f}')
print('=-'*20)


