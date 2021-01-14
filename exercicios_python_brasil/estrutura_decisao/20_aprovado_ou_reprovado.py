print('\033[1m>>> MÉDIA ARITMÉTICA <<<\033[m')
n1 = float(input('NOTA 1: '))
n2 = float(input('NOTA 2: '))
n3 = float(input('NOTA 3: '))
media = (n1+n2+n3)/3
print(f'MÉDIA: \033[1m{media:.2f}\033[m')
if media == 10:
    print(f'APROVADO COM DISTINÇÃO!')
elif media < 7:
    print(f'REPROVADO!')
else:
    print(f'APROVADO!')
