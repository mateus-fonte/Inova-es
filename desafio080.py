valores = []
menor = maior = 0
for valor in range(0, 5):
    v = int(input('Digite um valor: '))
    if valor == 0:
        valores.append(v)
        maior = v
        menor = v
        print('Adicionado ao final da lista...')
    else:
        if v > maior:
            maior = v
            valores.append(v)
            print('Adicionado ao final da lista...')
        if v < menor:
            menor = v
            valores.insert(0, v)
            print('Adicionado na posição 0 da lista...')
        if maior > v > menor:
            valores.insert(valor - 1, v)
            print(f'Adicionado na posição {valores.index(v)}')
print(f'A lista formada com os valores digitados em forma crescente é {valores}')

