print('\033[1m>>> VERIFICAÇÃO DE MULTA - ESTADO DE SP <<<\033[m')
peso = float(input('PESO DA CARGA (kg): '))
if peso > 50:
    excedente = peso-50
    multa = excedente*4
    print('\033[1:31mCARGA EXCEDENTE!\033[m')
    print(f'MULTA: \033[1mR$ {multa:.2f}\033[0m')
    print(f'>> {excedente:.2f} kg a mais que o limite estabelecido.')

else:
    print('\033[1:32mSEM CARGA EXCEDENTE!\033[m')
    print('SEM MULTAS!')
