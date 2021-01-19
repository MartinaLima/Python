num = int(input('- Informe um número para ver sua tabuada: '))
print(f'\033[1m>>> TABUADA DE {num} <<<\033[m')
for c in range(10):
    c += 1
    tabuada = num * c
    print(f'{num} X {c} = {tabuada}')
