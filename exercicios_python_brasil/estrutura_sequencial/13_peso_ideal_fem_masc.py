print('\033[1m>>> PESO IDEAL <<<\033[m')
sexo = str(input('INFORME O SEXO: [F/M] ').upper())
a = float(input('INFORME A ALTURA (m): '))
print('\033[1m\033[4mRESULTADO\033[m:')
if sexo in 'F':
    peso = (62.1*a)-44.7
    print(f'PESO IDEAL: \033[1:33m{peso:.2f}kg')
elif sexo in 'M':
    peso = (72.7*a)-58
    print(f'PESO IDEAL: \033[1:33m{peso:.2f}kg')
else:
    print('SEXO INVÁLIDO!')
