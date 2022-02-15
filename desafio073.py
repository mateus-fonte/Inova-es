tabela = ('' 'Atlético Mineiro', 'Flamengo', 'Palmeiras', 'Corinthians', 'RB Bragantino',
'Fortaleza', 'Fluminense', 'Ceará', 'Internacional', 'America-MG',
'Santos', 'São Paulo', 'Cuiabá', 'Athletico Paranaense',
'Atlético GO', 'Bahia', 'Juventude', 'Grêmio', 'Sport', 'Chape' '')
for c in range(0, 5):
    print(f'{c+1}º {tabela[c]}')
print('»'*20)
for c in range(16,20):
    print(f'{c+1}º {tabela[c]}')
print('»'*20)
print(sorted(tabela))
print('»'*20)
for c in range(19, 20):
    print(f'A Chapecoense está em {tabela.index("Chape")+1}º lugar')
