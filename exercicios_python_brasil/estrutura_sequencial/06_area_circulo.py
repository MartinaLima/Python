from math import pow, pi
print('\033[1m>>> ÁREA DO CÍRCULO <<<\033[m')
raio = float(input('Informe o raio do círculo: '))
area = pi * pow(raio, 2)
print(f'A área do círculo é igual a \033[1m{area:.2f}.')
