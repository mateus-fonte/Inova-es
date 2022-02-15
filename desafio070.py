soma = maisde8mil = c = cont = 0
barato = ''
while True:
    produto = str(input('Digite o nome de um produto: ')).title().strip()
    preço = float(input('Digite o preço desse produto: R$'))
    cont += 1
    soma += preço
    if cont == 1:
        menor = preço
        barato = produto
    if preço < menor:
        menor = preço
        barato = produto
    if preço > 1000:
        maisde8mil += 1
    continuar = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total gasto foi igual a R${soma:.2f}\n{maisde8mil} produtos custam mais de R$1000,00\nE o produto mais barato é o(a) {barato} que custa R${menor:.2f}')
