conthomem = maior = mulhermaior = 0
while True:
    i = int(input('Digite sua idade: '))
    s = ' '
    c = ' '
    while s not in 'MF':
        s = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    if i >= 18:
        maior += 1
    if s == 'M':
        conthomem += 1
    if s == 'F' and i < 20:
        mulhermaior += 1
    while c not in 'SN':
        c = input('Você quer continuar? ').upper().strip()[0]
    if c == 'N':
        break
print(f'No total temos {maior} pessoas maior de idade, {conthomem} homens e {mulhermaior} mulheres com menos de 20 anos!')
