print('{:^60}'.format('\033[1m ACADEMIA - PESQUISA \033[m'))
print('-'*50)
tot_clientes = 0
soma_alt = 0
soma_peso = 0
while True:
    tot_clientes += 1
    codigo = int(input(f'- Código {tot_clientes}º cliente: '))
    while codigo < 0:
        print('CÓDIGO INVÁLIDO!!!!')
        codigo = int(input(f'- Código {tot_clientes}º cliente: '))
    if codigo == 0:
        break
    altura = float(input('- Altura (m): '))
    peso = float(input('- Peso (kg): '))
    print('-'*25)
    soma_alt += altura
    soma_peso += peso
    if tot_clientes == 1:
        maior_alt = altura
        alto = codigo
        menor_alt = altura
        baixo = codigo
        maior_peso = peso
        pesado = codigo
        menor_peso = peso
        menos_pesado = codigo
    else:
        if altura > maior_alt:
            maior_alt = altura
            alto = codigo
        if altura < menor_alt:
            menor_alt = altura
            baixo = codigo
        if peso > maior_peso:
            maior_peso = peso
            pesado = codigo
        if peso < menor_peso:
            menor_peso = peso
            menos_pesado = codigo
if soma_alt == 0 or soma_peso == 0:
    print('-'*50)
else:
    media_alt = soma_alt / (tot_clientes - 1)
    media_peso = soma_peso / (tot_clientes - 1)
    print('-'*50)
    print('{:^50}'.format('RESULTADOS'))
    print('-' * 50)
    print(f' PARTICIPANTE(S): {tot_clientes-1}')
    print(f'> Cliente mais alto: {alto} - Altura: {maior_alt} m')
    print(f'> Cliente mais baixo: {baixo} - Altura: {menor_alt} m')
    print(f'> Cliente com maior peso: {pesado} - Peso: {maior_peso} kg')
    print(f'> Cliente com menor peso: {menos_pesado} - Peso: {menor_peso} kg')
    print(f'> Média alturas: {media_alt:.2f} m')
    print(f'> Média pesos: {media_peso:.2f} kg')
