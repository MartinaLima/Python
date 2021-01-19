print('\033[1m>>> CONTAGEM VERTICAL <<<\033[m')
for c in range(20):
    c += 1
    print(f'{c}...')
print('\033[1m>>> CONTAGEM HORIZONTAL <<<\033[m')
for c in range(20):
    c += 1
    print(c, end='... ')
