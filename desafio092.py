import datetime
info = {'nome': '', 'idade': '', 'Carteira': '', 'contratação': '', 'salario': '', 'aposentadoria': ''}
hj = datetime.date.today().year
for c in range(0, 1):
    info['nome'] = str(input('Nome: '))
    info['idade'] = hj - int(input('Ano de nascimento: '))
    info['Carteira'] = int(input('Carteira de trabalho (0 não tem): '))
    if info['Carteira'] == 0:
        break
    else:
        info['contratação'] = int(input('Ano de contratação: '))
        info['salario'] = float(input('Salário: '))
info['aposentadoria'] = info['idade']-(hj - info['contratação']) + 35
print('=-'*30)
print(info)
for k, v in info.items():
    if v == '':
        break
    print(f'{k} tem o valor {v}')

