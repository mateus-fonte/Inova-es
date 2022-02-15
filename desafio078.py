valores = []
maior = menor = 0
for contador in range(0, 5):
    valores.append(float(input(f'Digite um valor para a posição {contador}: ')))
    if contador == 0:
        menor = maior = valores[contador]
    else:
        if valores[contador] > maior:
            maior = valores[contador]
        if valores[contador] < menor:
            menor = valores[contador]
print('»'*50)
print(f'Você digitou os valores: {valores}')
print(f'O maior valor digitado foi o {maior} nas posições', end=' ')
for i, valor in enumerate(valores):
    if valor == maior:
        print(f'{i}»»', end='')
print()
print(f'O menor valor digitado foi o {menor} nas posições', end=' ')
for i, valor in enumerate(valores):
    if valor == menor:
        print(f'{i}»»', end='')
