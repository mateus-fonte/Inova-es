import random, emoji , time
janken = ['pedra', 'papel', 'tesoura']
a = random.choice(janken)
n = input('Ganhe de mim se for capaz, escolha pedra, papel, ou tesoura:')
print('JÓ')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PÔ')
time.sleep(1)
print('-='*15)
print(f'Computador jogou {a}')
print(f'Jogador jogou {n}')
print('-='*15)
if a == 'pedra' and n == 'tesoura' or a == 'tesoura' and n == 'papel' or a == 'papel' and n == 'pedra':
    print('HAHAHA, não foi desta vez, boa sorte na próxima, perdedor {}'.format(emoji.emojize(':stuck_out_tongue_closed_eyes:', use_aliases=True)))
elif a == 'pedra' and n == 'papel' or a == 'tesoura' and n == 'pedra' or a == 'papel' and n == 'tesoura':
    print('Você é muito bom nesse jogo, tenho que admitir {}'.format(emoji.emojize(':clap:', use_aliases=True)))
elif a == n:
    print('Empatamos dessa vez, mas só dessa vez, a proxima é minha {}'.format(emoji.emojize(':triumph:', use_aliases=True)))