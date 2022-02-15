from random import choice
a1 = str(input('Qual o nome do aluno1?'))
a2 = str(input('Qual o nome do aluno2?'))
a3 = str(input('Qual o nome do aluno3?'))
a4 = str(input('Qual o nome do aluno4?'))
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print(f'O escolhido foi {escolhido}')
