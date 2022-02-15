numeros = list()
def somaPar():
    soma = 0
    for c in numeros:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {numeros}, temos {soma} ')


def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    from random import randint
    import time
    for c in range(0, 6):
        numeros.append(randint(0, 10))
        print(numeros[c], end=' ')
        time.sleep(0.5)
    print('PRONTO!')


def main():
    sorteia()
    somaPar()
main()
