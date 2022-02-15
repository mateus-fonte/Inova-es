info = {'nome': '', 'gols': [], 'total': 0}
info['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {info["nome"]} jogou? '))
for g in range(0, partidas):
    info['gols'].append(int(input(f'Quantos gols na partida{g+1}? ')))
    info['total'] += info['gols'][g]
print('-='*30)
print(info)
print('-='*30)
for k, v in info.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {info["nome"]} jogou {partidas} partidas.')
for c in range(0, partidas):
    print(f'  => Na partida {c+1}, fez {info["gols"][c]} gols.')
print(f'Foi um total de {info["total"]} gols.')