from time import sleep
print('\033[1m>>> COMPARADOR DE PREÇOS <<<\033[m')
print('INFORME OS PREÇOS PARA COMPARAÇÃO:')
p1 = float(input('- PRODUTO 1: R$ '))
p2 = float(input('- PRODUTO 2: R$ '))
p3 = float(input('- PRODUTO 3: R$ '))
print('\033[1mBUSCANDO MENOR PREÇO...\033[m')
sleep(1)
print('\033[4mRESULTADO ENCONTRADO: \033[m')
if p1 < p2 and p1 < p3:
    print(f'PRODUTO 1 = \033[1mR$ {p1:.2f}')
elif p2 < p1 and p2 < p3:
    print(f'PRODUTO 2 = \033[1mR$ {p2:.2f}')
elif p3 < p1 and p3 < p2:
    print(f'PRODUTO 3 = \033[1mR$ {p3:.2f}')
elif p1 == p2 and p2 == p3:
    print('OS PRODUTOS POSSUEM O MESMO PREÇO! ')
elif p1 == p2:
    print(f'PRODUTOS 1 E 2 (MESMO PREÇO) = \033[1mR$ {p1:.2f}')
elif p1 == p3:
    print(f'PRODUTOS 1 E 3 (MESMO PREÇO) = \033[1mR$ {p1:.2f}')
elif p2 == p3:
    print(f'PRODUTOS 2 E 3 (MESMO PREÇO) = \033[1m$ {p2:.2f}')
