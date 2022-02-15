num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
escolha = int(input('''Digite a operação desejada
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Sua opção: '''))
while escolha != 5:
    if escolha == 1:
        print(num1 + num2)
    if escolha == 2:
        print(num1 * num2)
    if escolha == 3:
        if num1 > num2:
            print(num1)
        if num1 == num2:
            print('ambos os números são iguais')
        if num2 > num1:
            print(num2)
    if escolha == 4:
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))
    escolha = int(input('''Digite a operação desejada
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    Sua opção: '''))
print('Fim')
