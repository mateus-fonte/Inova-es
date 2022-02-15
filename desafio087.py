somapar = soma3coluna = maior = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if c == 2:
            soma3coluna += matriz[l][c]
        if l == 1 and c == 0:
            maior = matriz[l][c]
        if l == 1 and c != 0 and matriz[l][c] > maior:
            maior = matriz[l][c]
print('«»'*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('«»'*30)
print(f'A soma de todos os valores pares foi {somapar}')
print(f'A soma dos valores da terceira coluna foi {soma3coluna}')
print(f'O maior valor da segunda linha foi {maior}')
