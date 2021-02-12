print('{:^30}'.format('* COMPETIÇÃO DE GINÁSTICA *'))
cont_atleta = 0
while True:
    print('-'*30)
    tot_notas = list()
    atleta = str(input(f'Atleta {cont_atleta+1}: ').strip())
    while atleta == '':
        atleta = str(input(f'Atleta {cont_atleta + 1}: ').strip())
    for jurado in range(7):
        nota = float(input(f'Nota Jurado {jurado+1}: '))
        tot_notas.append(nota)
    outras_notas = [] + tot_notas
    outras_notas.remove(max(outras_notas))
    outras_notas.remove(min(outras_notas))
    media = sum(outras_notas) / 5
    print('-'*30)
    print('\033[1mRESULTADO:\033[m')
    print(f'* Atleta: {atleta.upper()}')
    print(f'* Melhor nota: {max(tot_notas)}')
    print(f'* Pior nota: {min(tot_notas)}')
    print(f'* Média notas: {media:.2f}')
    print('-'*30)
    continuar = str(input('Avaliar novo atleta [S/N]? ').upper())
    while continuar not in ['S', 'N']:
        continuar = str(input('Avaliar novo atleta [S/N]? ').upper())
    if continuar == 'N':
        print('Fim!')
        break
