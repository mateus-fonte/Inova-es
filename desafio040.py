n1 = float(input('Digite sua primeira nota:'))
n2 = float(input('Digite sua segunda nota:'))
m = (n1+n2)/2
if m < 5.0:
    print('Seu desempenho não foi suficiente, boa sorte ano que vem')
elif 6.9 > m > 5.0:
    print('Você vai para a recuperação')
elif m >= 7.0:
    print('Parabéns! Você passou direto')