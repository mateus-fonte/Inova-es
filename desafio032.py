from datetime import date
b = int(input('Digite um ano, se quiser analisar o ano atual digite 0:'))
if b == 0:
    b = date.today().year
if b % 4 == 0 and b % 100 != 0 or b % 400 ==0:
    print('O ano digitado é bissexto!')
else:
    print('O ano digitado não é bissexto!')
