from random import choice
c = tot =''
l = list(range(0, 10))
print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)
banana = 1
cont = 0
while banana == 1:
    escolha = choice(l)
    jogada = int(input('Digite um valor: '))
    opção = str(input('Par ou Ímpar? [P/I] ')).strip().lower()
    x = escolha + jogada
    if x % 2 == 1:
        tot = 'DEU ÍMPAR'
    if x % 2 == 0:
        tot = 'DEU PAR'
    print('-'*40)
    print(f'Você escolheu {jogada} e o computador {escolha}. Total de {x} {tot}')
    print('-'*40)
    if opção == 'p':
        c = 'i'
    if opção == 'i':
        c = 'p'
    totp = x % 2
    jogp = jogada % 2
    if totp == 0 and opção == 'p' or totp == 1 and opção == 'i':
        print('Você VENCEU!')
        cont += 1
    if totp != 0 and c == 'i' or totp == 0 and c == 'p':
        banana = 0
        print('Você PERDEU!')
        print('»'*32)
print(f'GAME OVER! Você venceu {cont} vezes.')


