print('\033[1m * ACIDENTES DE TRÂNSITO - 1999 *\033[m')
tot_cidades = 0
soma_acidentes = 0
cidades_peq = 0
soma_veiculos = 0
for tot_cidades in range(5):
    tot_cidades += 1
    codigo = int(input(f'Código cidade {tot_cidades}: '))
    while codigo <= 0:
        print('CÓDIGO INVÁLIDO!!!')
        codigo = int(input(f'Código cidade {tot_cidades}: '))
    veiculos = int(input('Veículos de passeio: '))
    acidentes = int(input('Acidentes com vítimas: '))
    print('-'*35)
    if veiculos <= 2000:
        soma_acidentes += acidentes
        cidades_peq += 1
    if tot_cidades == 1:
        mais_acidentes = acidentes
        cidade_mais = codigo
        menos_acidentes = acidentes
        cidade_menos = codigo
    else:
        if acidentes > mais_acidentes:
            mais_acidentes = acidentes
            cidade_mais = codigo
        elif acidentes == mais_acidentes:
            cidade_mais = 'há mais de uma cidade com o maior índice de acidentes!'
        if acidentes < menos_acidentes:
            menos_acidentes = acidentes
            cidade_menos = codigo
        elif acidentes == menos_acidentes:
            cidade_menos = 'há mais de uma cidade com o menor índice de acidentes!'
    soma_veiculos += veiculos
media_veiculos = soma_veiculos/tot_cidades
media_acidentes = soma_acidentes / cidades_peq
print('{:^35}'.format('RESULTADOS DA PESQUISA'))
print('-' * 35)
print(f'MÉDIA GERAL DE VEÍCULOS: {media_veiculos:.2f}')
print('MAIOR ÍNDICE DE ACIDENTES:')
print(f'* Cidade: {cidade_mais}')
print(f'* Acidentes: {mais_acidentes}')
print('MENOR ÍNDICE DE ACIDENTES:')
print(f'* Cidade: {cidade_menos}')
print(f'* Acidentes: {menos_acidentes}')
print('MÉDIA ACIDENTES:')
print(f'* Cidades com até 2000 veículos: {media_acidentes:.2f}')
