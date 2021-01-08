print('\033[1m>>> SALÁRIO MENSAL <<<\033[m')
print('Por favor, preencha os campos a seguir.')
valor_hora = float(input('VALOR HORA: R$ '))
hora = float(input('HORAS TRABALHADAS: '))
total = hora*valor_hora
print('-'*30)
print('\033[1mRESULTADO:\033[m')
print(f'SALÁRIO BRUTO: \033[1mR$ {total:.2f}')
