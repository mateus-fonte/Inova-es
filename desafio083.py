expressao = input('Digite uma expressão: ').strip()
pilha = []
for p in expressao:
    if p == '(':
        pilha.append('(')
    elif p == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está valida')
else:
    print('Sua expressão está invalida')