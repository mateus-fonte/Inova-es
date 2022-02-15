n1 = int(input('Digite um número: '))
continuar = str(input('Você quer continuar [S/N]? '))
menor = maior = soma = média = n3 = n1
cont = 1
while continuar in 'Ss':
        n2 = int(input('Digite um número: '))
        continuar = str(input('Você quer continuar [S/N]? ')).upper().strip()[0]
        if n2 > n1:
            maior = n2
        if n2 < n1:
            menor = n2
        soma = n2 + n3
        n3 = soma
        cont += 1
        média = soma / cont
print('A média entre os {} números foi {}'.format(cont, média))
print('O Maior número digitado foi o {} e o Menor foi o {}'.format(maior, menor))

