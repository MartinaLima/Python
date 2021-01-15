print('\033[1m<< INFORME DOIS VALORES >>\033[m')
n1 = float(input('1º VALOR: '))
n2 = float(input('2º VALOR: '))
print('ESCOLHA A OPERAÇÃO:')
opcao = int(input('[1] SOMA\n[2] SUBTRAÇÃO\n[3] MULTIPLICAÇÃO\n[4] DIVISÃO\n---> '))

if opcao in [1, 2, 3, 4]:
    if opcao == 1:
        total = n1 + n2
    elif opcao == 2:
        total = n1 - n2
    elif opcao == 3:
        total = n1 * n2
    else:
        total = n1 / n2
    print(f'RESULTADO... = {total:.2f}')
    print('ESTE É UM NÚMERO',end=' ')
    if total % 2 == 0:
        print('PAR',end=', ')
    else:
        print('ÍMPAR',end=', ')
    if total < 0:
        print('NEGATIVO',end=' ')
    else:
        print('POSITIVO',end=' ')
    if total == round(total):
        print('E INTEIRO!')
    else:
        print('E DECIMAL!')
else:
    print('OPERAÇÃO INVÁLIDA!')
