print('{:^30}'.format('ELEIÇÕES'))
print('º' * 30)
print('     1   | CANDIDATO 1\n'
      '     2   | CANDIDATO 2\n'
      '     3   | CANDIDATO 3\n'
      '     4   | CANDIDATO 4\n'
      '     5   | NULO\n'
      '     6   | EM BRANCO')
print('-' * 30)
tot_votos = 0
cand_a = 0
cand_b = 0
cand_c = 0
cand_d = 0
nulo = 0
branco = 0
while True:
    tot_votos += 1
    voto = int(input('- Código ou 0 para finalizar: '))
    while voto not in (0, 1, 2, 3, 4, 5, 6):
        print('CÓDIGO INVÁLIDO!')
        voto = int(input('- Código ou 0 para finalizar: '))
    if voto == 0:
        print('Finalizando...')
        break
    elif voto == 1:
        cand_a += 1
    elif voto == 2:
        cand_b += 1
    elif voto == 3:
        cand_c += 1
    elif voto == 4:
        cand_d += 1
    elif voto == 5:
        nulo += 1
    else:
        branco += 1
porce_nulo = (nulo*100)/(tot_votos - 1)
porce_branco = (branco*100)/(tot_votos - 1)
print('-' * 30)
print('{:^30}'.format('RESULTADO'))
print('º' * 30)
print(f'TOTAL DE VOTOS: {tot_votos-1}')
print(f'* Candidato 1:  {cand_a} ')
print(f'* Candidato 2:  {cand_b} ')
print(f'* Candidato 3:  {cand_c} ')
print(f'* Candidato 4:  {cand_d} ')
print(f'* Nulos ({porce_nulo:.2f}%):  {nulo}')
print(f'* Em branco ({porce_branco:.2f}%):  {branco}')
