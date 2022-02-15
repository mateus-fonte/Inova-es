nome = str(input('Digite seu nome:')).strip()
print('Analisando seu nome')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print('seu nome tem ao todo ', len(nome)-nome.count(' '), 'letras')
divide = nome.split()
print('seu primeiro nome é {} e ele tem {} letras '.format(divide[0], len(divide[0])))


