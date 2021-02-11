print('{:^40}'.format('* COMPETIÇÃO DE SALTO EM DISTÂNCIA *'))
atletas = 0
while True:
    atletas += 1
    print('-' * 40)
    print(f'ATLETA {atletas}:')
    tot_dist = list()
    soma_dist = 0
    nome = str(input('Nome: ').upper().strip())
    if nome == '':
        print('Finalizado!')
        break
    for c in range(5):
        distancia = float(input(f'{c+1}º salto: '))
        tot_dist.append(distancia)
    outras_dist = [] + tot_dist
    outras_dist.remove(max(outras_dist))
    outras_dist.remove(min(outras_dist))
    soma_dist = sum(outras_dist)
    media = soma_dist / 3
    print('\033[1mRESULTADO >>> \033[m')
    print(f'* Atleta: {nome}')
    print(f'* Média distâncias: {media:.2f} m')
    print(f'* Melhor salto: {max(tot_dist)} m')
    print(f'* Pior salto: {min(tot_dist)} m')
