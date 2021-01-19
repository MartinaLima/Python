print('\033[1m>>> SOMA E MÉDIA <<<\033[m')
soma = 0
c = 0
for c in range(5):
    c += 1
    num = int(input(f'- {c}º VALOR: '))
    soma += num
media = soma/c
print(f'A SOMA DOS VALORES É: {soma}')
print(f'A MÉDIA DOS VALORES É: {media:.2f}')
