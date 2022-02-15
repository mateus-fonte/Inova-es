valores = []
while True:
    v = int(input('Digite um valor: '))
    valores.append(v)
    e = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
    if e in 'Nn':
        break
valores.sort(reverse=True)
print(f'{len(valores)} números foram digitados!')
print(f'A lista escrita em ordem decrescente é: {valores}')
if 5 in valores:
    print('O valor 5 FOI digitado e está na lista!')
else:
    print('O valor 5 NÃO FOI digitado!')