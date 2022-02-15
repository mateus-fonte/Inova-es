palavras = ('Campus', 'Universidade', 'Engenharia', 'Programação', 'Matematica',
            'Computador', 'Cantina', 'Professor', 'Avaliação', 'Recurso', 'Bbiblioteca', 'UA')
for p in palavras:
    print(f'\nNa palavra {p} temos', end=' ')
    for vogal in p:
        if vogal.lower() in 'aeiou':
            print(vogal, end=' ')

