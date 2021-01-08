print('\033[1m>>> CONVERSOR DE TEMPERATURA <<<\033[m')
c = float(input('Informe a temperatura em Célsius: '))
f = c*1.8+32
print('-'*40)
print('\033[1mRESULTADO:\033[m')
print(f'{c:.1f}º Célsius = \033[1m{f:.1f}º Fahrenheit')
