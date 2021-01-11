print('\033[1m>>> MÉDIA ARITMÉTICA <<<\033[m')
n1 = float(input('1ª NOTA: '))
n2 = float(input('2ª NOTA: '))
media = (n1+n2)/2
print('\033[1mRESULTADO FINAL:\033[m')
if media >= 7 and media <10:
    print(f'MÉDIA: {media:.2f}.')
    print('APROVADO!')
elif media < 7:
    print(f'MÉDIA: {media:.2f}.')
    print('REPROVADO!')
elif media == 10:
    print(f'MÉDIA: {media:.2f}.')
    print('APROVADO COM DISTINÇÃO!')
