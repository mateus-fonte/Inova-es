n1 = float(input('Digite um número:'))
n2 = float(input('Digite outro:'))
n3 = float(input('Pra terminar:'))
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
menor = n1
if n2 < n1 and n2 < n3:
    n2 = menor
if n3 < n1 and n3 < n2:
    n3 = menor
print('O menor número é o {} e o maior é o {}'.format(menor, maior))
