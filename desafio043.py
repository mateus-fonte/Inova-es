p = float(input('Digite seu peso em kgs:'))
a = float(input('Digite sua altura em metros:'))
IMC = p/a**2
print('O IMC dessa pessoa é {:.2f}'.format(IMC))
if IMC < 18.5:
    print('Você está abaixo do peso ideal')
elif 25 > IMC >= 18.5:
    print('Você está com o peso ideal, continue assim!')
elif 30 > IMC >= 25:
    print('Você está com sobrepeso')
elif 40 > IMC >= 30:
    print('Você está obeso')
else:
    print('Você está com obesidade mórbida')