a = int(input('Digite o ano em que você nasceu:'))
i = 2021-a
if i < 18:
    print(f'Você ainda tem {18-i} anos até se alistar')
elif i == 18:
    print('Você está em tempo de se alistar')
elif i > 18:
    print(f'Já passaram {i-18} anos do prazo do seu alistamento')