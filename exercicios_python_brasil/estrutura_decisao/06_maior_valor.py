print('\033[1mINFORME 3 VALORES PARA DESCOBRIR QUAL O MAIOR!\033[m')
n1 = int(input('>> 1º VALOR: '))
n2 = int(input('>> 2º VALOR: '))
n3 = int(input('>> 3º VALOR: '))
print('\033[1mRESULTADO...\033[m')
if n1 > n2 and n1 > n3:
    print(f'MAIOR VALOR: {n1}.')
elif n2 > n1 and n2 > n3:
    print(f'MAIOR VALOR: {n2}.')
elif n3 > n1 and n3 > n2:
    print(f'MAIOR VALOR: {n3}.')
else:
    print('AO MENOS DOIS VALORES SÃO IGUAIS!')
