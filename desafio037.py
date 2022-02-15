n = int(input('Digite um número em base 10:'))
b = int(input('Escolha uma das bases para conversão:\n[ 1 ] Converter para BINÁRIO\n[ 2 ] Converter para OCTAL\n[ 3 ] Converter para HEXADECIMAL\nSua opção:'))
if b == 1:
    print(f'{n} convertido para BINÁRIO é igual a {bin(n)[2:]}')
elif b == 2:
    print(f'{n} convertido para OCTAL é igual a {oct(n)[2:]}')
elif b == 3:
    print(f'{n} convertido para HEXADECIMAL é igual a {hex(n)[2:]}')