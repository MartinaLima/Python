print('\033[1m>>> CONVERSOR DE TEMPERATURA <<<\033[m')
f = float(input('Informe a temperatura em Fahrenheit: '))
c = 5*((f-32)/9)
print('-'*40)
print('\033[1mRESULTADO:\033[m')
print(f'{f:.2f}º Fahrenheit = \033[1m{c:.2f}º Célsius')
