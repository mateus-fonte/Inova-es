pessoas = []
soma = 0
mulheres = []
maiores = []
while True:
    pessoax = {'nome': '', 'sexo': '', 'idade': 0}
    pessoax['nome'] = str(input('Nome: '))
    pessoax['sexo'] = str(input('Sexo: [F/M] ')).strip().upper()[0]
    if pessoax['sexo'] == 'F':
        mulheres.append(pessoax["nome"])
    pessoax['idade'] = int(input('Idade: '))
    soma += pessoax['idade']
    pessoas.append(pessoax)
    opcao = str(input('Quer continuar? [S/N] '))[0]
    if opcao in 'Nn':
        break
media = soma / len(pessoas)
print('=-'*30)
print(f'>> O grupo tem {len(pessoas)} pessoas.')
print(f'>> A média de idade é de {media} anos.')
if len(mulheres) != 0:
    print(f'>> As mulheres cadastradas foram: {mulheres}')
for c, p in enumerate(pessoas):
    if pessoas[c]["idade"] >= media:
        maiores.append(pessoas[c]["nome"])
print(f'>> Lista das pessoas que estão acima da média: {maiores}')

