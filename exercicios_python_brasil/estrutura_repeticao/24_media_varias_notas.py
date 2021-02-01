print('>>> Informe as notas:')
c = 0
soma = 0
continua = ''
while continua != 'N':
    c += 1
    nota = float(input(f'- NOTA {c}: '))
    soma += nota
    continua = str(input('Continuar? [S/N]: ').upper())
    while continua not in 'S' and continua not in 'N':
        continua = str(input('Continuar? [S/N]: ').upper())
if soma == 0:
    media = 0
else:
    media = soma / c
print('OPERAÇÃO FINALIZADA!')
print('RESULTADO:')
print(f'MÉDIA GERAL: {media:.2f}')
