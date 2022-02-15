aluno = {'nome': '', 'média': 0, 'situação': ''}
aluno['nome'] = str(input('Nome: ')).title()
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
print(f'Nome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["média"]}')
if aluno["média"] >= 7:
    aluno["situação"] = 'aprovado'
else:
    aluno["situação"] = 'reprovado'
print(f'Situação é igual a {aluno["situação"]}')

