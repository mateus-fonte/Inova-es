import random
lista = [0, 1, 2, 3, 4, 5]
n = random.choice(lista)
m = int(input('Digite um número entre 0 e 5:'))
if m == n:
    print('Parabéns você acertou o número')
else:
    print('Não foi desta vez, tente mais tarde')

