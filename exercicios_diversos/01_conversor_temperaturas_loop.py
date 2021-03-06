print('\033[1m>>> CONVERSOR DE TEMPERATURAS <<< \033[m')
escolha = ''
while escolha != 'N':
    temp = float(input('Informe a temperatura: '))
    opcao = int(input('Escolha o tipo de conversão:\n'
                      '[1] Celsius para Fahrenheit\n'
                      '[2] Celsius para Kelvin\n'
                      '[3] Fahrenheit para Celsius\n'
                      '[4] Fahrenheit para Kelvin\n'
                      '[5] Kelvin para Celsius\n'
                      '[6] Kelvin para Fahrenheit\n'
                      '---> '))
    tipo1 = ''
    tipo2 = ''
    resultado = 0
    if opcao in (1, 2, 3, 4, 5, 6):
        if opcao == 1:
            tipo1 = '° Celsius'
            tipo2 = '° Fahrenheit'
            resultado = 1.8 * temp + 32
        elif opcao == 2:
            tipo1 = '° Celsius'
            tipo2 = ' Kelvin'
            resultado = 273.15 + temp
        elif opcao == 3:
            tipo1 = '° Fahrenheit'
            tipo2 = '° Celsius'
            resultado = (temp - 32) / 1.8
        elif opcao == 4:
            tipo1 = '° Fahrenheit'
            tipo2 = ' Kelvin'
            resultado = ((temp - 32) / 1.8) + 273.15
        elif opcao == 5:
            tipo1 = ' Kelvin'
            tipo2 = '° Celsius'
            resultado = temp - 273.15
        elif opcao == 6:
            tipo1 = ' Kelvin'
            tipo2 = '° Fahrenheit'
            resultado = 1.8 * (temp - 273.15) + 32
        print(f'RESULTADO:\n'
              f'{temp}{tipo1} é igual a {resultado:.2f}{tipo2}.')
    else:
        print('OPÇÃO INVÁLIDA!')
    escolha = str(input('Quer continuar? [S/N] ').upper())
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N] ').upper())
    if escolha == 'N':
        print('Fim do programa!')
