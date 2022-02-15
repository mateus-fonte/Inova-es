import datetime
data = datetime.date.today().year
totmaior = 0
totmenor = 0
for pessoa in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu?'.format(pessoa)))
    idade = data - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('''O número de maiores de idade é {}
e o número de menores de idade é {}'''.format(totmaior, totmenor))
