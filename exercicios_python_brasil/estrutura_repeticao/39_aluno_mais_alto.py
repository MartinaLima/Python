print('\033[1m>>> COMPARADOR DE ALTURAS <<<\033[m')
for tot_alunos in range(10):
    tot_alunos += 1
    codigo = int(input(f'Código aluno(a) {tot_alunos}: '))
    while codigo <= 0:
        print('CÓDIGO INVÁLIDO!!!')
        codigo = int(input(f'Código aluno(a) {tot_alunos}: '))
    altura = float(input('Altura (cm): '))
    print('-'*30)
    if tot_alunos == 1:
        maior = altura
        alto = codigo
        menor = altura
        baixo = codigo
    else:
        if altura > maior:
            maior = altura
            alto = codigo
        if altura < menor:
            menor = altura
            baixo = codigo
print('\033[1mRESULTADOS... \033[m')
print('-'*30)
print('\033[1mMAIS ALTO\033[m')
print(f'Código: {alto}')
print(f'Altura: {maior} cm')
print('\033[1mMAIS BAIXO\033[m')
print(f'Código: {baixo}')
print(f'Altura: {menor} cm')
