print('Informe um valor qualquer e eu lhe direi se é negativo ou positivo!')
num = int(input('----> '))
if num < 0:
    print(f'>> O valor {num} é \033[1mNEGATIVO!')
else:
    print(f'>> O valor {num} é \033[1mPOSITIVO!')
