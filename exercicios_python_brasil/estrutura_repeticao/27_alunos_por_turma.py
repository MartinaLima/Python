print('\033[1m>>> MÉDIA ALUNOS POR TURMA <<<\033[m')
print('-'*31)
turmas = int(input('* Quantidade de turmas: '))
tot_turmas = 0
tot_alunos = 0
for tot_turmas in range(turmas):
    tot_turmas += 1
    alunos = int(input(f'- Alunos turma {tot_turmas}: '))
    while alunos > 40:
        print('Quantidade excedente! Limite de alunos por turma é 40!')
        alunos = int(input(f'- Alunos turma {tot_turmas}: '))
    tot_alunos += alunos
media = tot_alunos / tot_turmas
print('-'*31)
print('\033[1mRESULTADO...\033[m')
print(f'MÉDIA DE ALUNOS POR TURMA: {media:.1f}')
