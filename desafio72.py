extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco'
    , 'seis', 'sete', 'oito', 'nove', 'dez'
    , 'onze', 'doze', 'treze', 'catorze', 'quinze'
    , 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = int(input('Digite um número entre 0 e 20 para ver seu nome por extenso: '))
while num not in range(0, len(extenso)):
    num = int(input('Digite um número entre 0 e 20 para ver seu nome por extenso: '))
print(f'o número {num} por extenso é {extenso[num]}')