print('{:^60}'.format('ELEIÇÕES'))
print('*' * 60)
eleitores = int(input('* QUANTIDADE DE ELEITORES: '))
print('-' * 60)
eleitor = 0
candidato = 0
cand1 = 0
cand2 = 0
cand3 = 0
for eleitor in range(eleitores):
    eleitor += 1
    candidato = int(input(f'Olá, Eleitor {eleitor}!\n'
                          'Informe o código do candidato desejado.\n'
                          '1000 - Candidato 1 | 2000 - Candidato 2 | 3000 - Candidato 3\n'
                          '=> '))
    while candidato not in (1000, 2000, 3000):
        candidato = int(input(f'CÓDIGO INVÁLIDO!\n'
                              'Informe o código do candidato desejado.\n'
                              '1000 - Candidato 1 | 2000 - Candidato 2 | 3000 - Candidato 3\n'
                              '=> '))
    print('Obrigado por votar! =)')
    print('-'*60)
    if candidato == 1000:
        cand1 += 1
    elif candidato == 2000:
        cand2 += 1
    else:
        cand3 += 1
print('{:^60}'.format('RESULTADO'))
print('*' * 60)
print(f'- VOTOS VÁLIDOS: {eleitor}')
print(f'- CANDIDATO 1: {cand1}')
print(f'- CANDIDATO 2: {cand2}')
print(f'- CANDIDATO 3: {cand3}')
