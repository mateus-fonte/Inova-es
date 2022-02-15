pessoa = []
galera = []
totpessoas = maiorpeso = menorpeso = 0
while True:
    pessoa.append(str(input('Nome: ')))
    p = float(input('Peso: '))
    pessoa.append(p)
    if len(galera) == 0:
        maiorpeso = p
        menorpeso = p
    if len(pessoa) == 2:
        if p > maiorpeso:
            maiorpeso = p
        if p < menorpeso:
            menorpeso = p
    galera.append(pessoa[:])
    pessoa.clear()
    totpessoas += 1
    option = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if option in 'N':
        break
print(f'Ao todo você cadastrou {totpessoas} pessoas')
print(f'O maior peso foi de {maiorpeso}kg. Peso de ', end='')
for p in range(0, len(galera)):
    if float(galera[p][1]) == maiorpeso:
        print(galera[p][0], end=' ')
print()
print(f'O menor peso foi de {menorpeso}kg. Peso de ', end='')
for p in range(0, len(galera)):
    if float(galera[p][1]) == menorpeso:
        print(galera[p][0], end=' ')



