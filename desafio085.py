valores = []
for c in range(0, 7):
    valor = int(input(f'Digite o {c+1}º valor: '))
    valores.append(valor)
valores.sort()
print('=-'*30)
print('Os valores pares digitados foram:', end=' ')
for c in range(0, 7):
    if valores[c] % 2 == 0:
        print(valores[c], end=' ')
print()
print('Os valores ímpares digitados foram:', end=' ')
for c in range(0, 7):
    if valores[c] % 2 != 0:
        print(valores[c], end=' ')
