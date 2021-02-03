print('\033[1m>>> MÉDIA DE IDADES <<<\033[m')
continuar = 'S'
totalunos = 0
totIdades = 0
while continuar != 'N':
    totalunos += 1
    idade = int(input(f'{totalunos}ª IDADE: '))
    totIdades += idade
    continuar = str(input('Continuar? [S/N]: ').upper())
    while continuar not in 'S' and continuar not in 'N':
        continuar = str(input('Continuar? [S/N]: ').upper())
media = totIdades / totalunos
if 0 <= media <= 25:
    categoria = 'JOVEM'
elif 26 <= media <= 60:
    categoria = 'ADULTA'
elif media > 60:
    categoria = 'IDOSA'
else:
    categoria = 'INDEFINIDA'
print('\033[1mRESULTADO...\033[m')
print(f'* MÉDIA GERAL DE IDADES: {media:.1f} anos')
print(f'* CATEGORIA DA TURMA: {categoria}')
