cont = cont9 = contpar = 0
lista = []
tuplapar = ()
for c in range(0, 4):
    n = (int(input('Digite um valor:')))
    cont += 1
    lista.append(n)
    if n == 9:
        cont9 += 1
tupla = lista
print(tupla)
if 9 in tupla:
    print(f'O valor 9 apareceu {cont9} vezes')
else:
    print('O valor 9 não apareceu nenhuma vez')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posição')
else:
    print('O valor 3 não apareceu nenhuma vez')
print(f'Os valores pares digitados foram', end=' ')
for num in tupla:
    if num % 2 == 0:
        contpar += 1
        print(num, end=' ')
