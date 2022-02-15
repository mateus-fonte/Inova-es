valores = list()
while True:
    c = int(input('Digite um valor: '))
    if c in valores:
        print('O valor ja foi digitado, logo, não foi adicionado novamente')
    else:
        valores.append(c)
        print('Valor adicionado com sucesso...')
    valores.sort()
    continua = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continua in 'Nn':
        break
print(valores)