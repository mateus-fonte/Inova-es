import random, time
MEGA = list()
cartela = list()
print('+'*30)
print(f'{"DAFÃO DO MILHÃO":^30}')
print('+'*30)
c = int(input('Quantos jogos você vai jogar? '))
for t in range(0, c):
    for c in range(0, 6):
        g = random.randint(1, 60)
        cartela.append(g)
        cartela.sort()
    MEGA.append(cartela[:])
    cartela.clear()
for y in range(0, len(MEGA)):
    print(f'Jogo {y+1}: {MEGA[y]}')
    time.sleep(1)