from random import shuffle
a1 = input('Qual o nome do aluno 1?')
a2 = input('Qual o nome do aluno 2?')
a3 = input('Qual o nome do aluno 3?')
a4 = input('Qual o nome do aluno 4?')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem de apresentação escolhida foi ')
print(lista)
