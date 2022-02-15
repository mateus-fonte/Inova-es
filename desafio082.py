valores = []
valorespares = []
valoresimpares = []
while True:
    v = int(input('Digite um valor: '))
    valores.append(v)
    e = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
    if e in 'N':
        break
for v in range(0, len(valores)):
    if valores[v] % 2 == 0:
        valorespares.append(valores[v])
    else:
        valoresimpares.append(valores[v])
print(f'A lista gerada foi {valores}')
print(f'A lista gerada pelos valores pares foi {valorespares}')
print(f'A lista gerada pelos valores ímpares foi {valoresimpares}')
