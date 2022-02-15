import random
num = ''
cont = maior = menor = 0
print(f'Os valores sorteados foram:{num} ', end='')
while cont < 5:
    numero = random.randint(0, 10)
    cont += 1
    if cont < 5:
        num = print(numero, end=' ')
    else:
        num = print(numero)
    if cont == 1:
        menor = numero
        maior = numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
print(f'O maior valor sorteado foi o {maior}')
print(f'O menor valor sorteado foi o {menor}')


