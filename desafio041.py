a = int(input('Digite seu ano de nascimento:'))
i = 2021 - a
if i <= 9:
    print('A categoria do atleta é Mirim')
elif 14 >= i > 9:
    print('A categoria do atleta é Infantil')
elif 19 >= i > 14:
    print('A categoria do atleta é Junior')
elif 20 >= i > 19:
    print('A categoria do atleta é Sênior')
else:
    print('A categoria do atleta é Master')
