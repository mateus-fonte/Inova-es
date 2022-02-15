print('Gerador de PA')
print('-=' * 10)
p1 = float(input('Digite o primeiro termo da PA: '))
r = float(input('Digite a razão da PA: '))
cont = 0
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont < total:
        print(p1, end=' » ')
        p1 = p1 + r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))

