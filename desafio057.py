sexo = input('Digite seu sexo [M/F]: ').upper().strip()
while sexo not in 'MF':
    print('Você digitou errado, tente novamente')
    sexo = input('Digite seu sexo [M/F]: ').upper().strip()
if sexo == 'M':
    print('Você é do sexo Masculino')
else:
    print('Você é do sexo feminino')
