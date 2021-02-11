print('{:^60}'.format('QUESTÕES DA PROVA'))
print('-'*60)
alunos = 0
todos_acertos = 0
mais_acertos = 0
menos_acertos = 0
aluno_mais = ''
aluno_menos = ''
while True:
    alunos += 1
    print('>> Informe seu nome e a resposta das questões [A, B, C, D, E].')
    nome = str(input('Nome: ').upper())
    c = 0
    tot_respostas = list()
    gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
    acertos = 0
    for c in range(10):
        c += 1
        resposta = str(input(f'Questão {c}: ').upper())
        while resposta not in ['A', 'B', 'C', 'D', 'E']:
            print('RESPOSTA INVÁLIDA!')
            resposta = str(input(f'Questão {c}: ').upper())
        tot_respostas.append(resposta)
    for letra in range(len(gabarito)):
        if tot_respostas[letra] == gabarito[letra]:
            acertos += 1
    print('-' * 30)
    print(f'NOTA: {acertos:.2f}')
    print(f'ACERTOS: {acertos}')
    print('-' * 30)
    if alunos == 1:
        mais_acertos = acertos
        menos_acertos = acertos
        aluno_mais = nome
        aluno_menos = nome
    else:
        if acertos > mais_acertos:
            mais_acertos = acertos
            aluno_mais = nome
        elif acertos == mais_acertos:
            aluno_mais = 'há mais de um aluno com mais acertos'
        if acertos < menos_acertos:
            menos_acertos = acertos
            aluno_menos = nome
        elif acertos == menos_acertos:
            aluno_menos = 'há mais de um aluno com menos acertos'
    todos_acertos += acertos
    novo_aluno = str(input('Continuar novo aluno [S/N]? ').upper())
    while novo_aluno not in ['S', 'N']:
        novo_aluno = str(input('Continuar novo aluno [S/N]? ').upper())
    if novo_aluno == 'N':
        break
media = todos_acertos / alunos
print('-' * 30)
print('RESULTADO...')
print(f'* Total de alunos: {alunos}')
print(f'* Média geral: {media:.2f}')
print(f'* Aluno com mais acertos: {aluno_mais}')
print(f'* Acertos: {mais_acertos}')
print(f'* Aluno com menos acertos: {aluno_menos}')
print(f'* Acertos: {menos_acertos}')
