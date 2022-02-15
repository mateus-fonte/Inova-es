import random, time , operator
jogadas = {'jogador1': random.randint(1, 6),
           'jogador2': random.randint(1, 6),
           'jogador3': random.randint(1, 6),
           'jogador4': random.randint(1, 6)}
ranking = []
print('Valores sorteados:')
for k, v in jogadas.items():
    print(f'O {k} tirou {v}')
    time.sleep(1)
print('Ranking dos jogadores:')
ranking = sorted(jogadas.items(), key=operator.itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    time.sleep(1)


