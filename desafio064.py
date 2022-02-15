num = int(input('Digite um número [999 para parar]: '))
soma = 0
termos = 0
while num != 999:
    soma = num + soma
    termos += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(termos, soma))
