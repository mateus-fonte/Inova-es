from random import choice
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
escolha = choice(lista)
num = int(input('Tente adivinhar que número eu estou pensando: '))
tot = 0
while escolha != num:
    num = int(input('ERRADO! Tente outra vez: '))
    tot += 1
print('Finalmente! parece que você não cansa de perder, voce precisou de {} palpites para acertar'.format(tot+1))
