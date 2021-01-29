""" Faça um programa que leia as três notas de vários alunos, calcule a média e informe se está APROVADO (acima de 
7 pontos), REPROVADO (abaixo de 6 pontos) ou em RECUPERAÇÃO (entre 6 e 7 pontos). Ao final, exiba na tela a 
quantidade de alunos aprovados, reprovados e em recuperação, a média total de todos os alunos e a média de todos os 
alunos APROVADOS. Ainda calcule a porcentagem de alunos em cada uma das categorias. """

print('\033[1m>>> PESQUISA DE APROVAÇÃO DE ALUNOS <<<\033[m')
ap = 0
rep = 0
rec = 0
opcao = ''
alunos = 0
media_ap = 0
media_total = 0
while opcao != 'N':
    alunos += 1
    print(f'\033[1mALUNO {alunos}\033[m')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    n3 = float(input('Nota 3: '))
    media = (n1+n2+n3)/3
    print(f'Média = {media:.2f}', end=' | ')
    if media > 7:
        print('APROVADO!')
        ap += 1
        media_ap += media
    elif media < 6:
        print('REPROVADO!')
        rep += 1
    else:
        print('RECUPERAÇÃO!')
        rec += 1
    media_total += media
    opcao = str(input('CADASTRAR MAIS ALUNOS? [S/N] ').upper())
    while opcao not in 'SN':
        opcao = str(input('CADASTRAR MAIS ALUNOS? [S/N] ').upper())
if ap >= 1:
    media_aprovados = media_ap/ap
else:
    media_aprovados = 0
print('-'*40)
print('\033[1mRESULTADOS...\033[m')
print(f'* Quantidade de alunos: {alunos}')
print(f'* Alunos aprovados {(ap*100)/alunos:.1f}%: {ap}')
print(f'* Alunos reprovados {(rep*100)/alunos:.1f}%: {rep}')
print(f'* Alunos em recuperação {(rec*100)/alunos:.1f}%: {rec}')
print(f'* Média geral: {media_total/alunos:.2f}')
print(f'* Média aprovados: {media_aprovados:.2f}')
