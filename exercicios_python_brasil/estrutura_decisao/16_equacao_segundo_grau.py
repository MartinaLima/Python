from math import pow, sqrt

print('\033[1m>>> EQUAÇÃO DE 2º GRAU <<<\033[m')
a = int(input('> VALOR DE A: '))
if a != 0:
    b = int(input('> VALOR DE B: '))
    c = int(input('> VALOR DE C: '))
    print('-'*30)
    print('\033[1mRESULTADO...\033[m')
    delta = pow(b, 2) - (4 * a * c)
    if delta > 0:
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
        print(f'X1 = {x1:.4f}\nX2 = {x2:.4f}')
    elif delta == 0:
        x1 = -b / (2 * a)
        print(f'X = {x1:.2f}')
    elif delta < 0:
        print('-> A EQUAÇÃO NÃO POSSUI RAÍZES!')
else:
    print('-> A EQUAÇÃO NÃO É DE SEGUNDO GRAU QUANDO A = 0!')
