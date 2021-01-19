print('\033[1m>>> PARES E ÍMPARES <<<\033[m')
print('Informe 10 valores!')
c = 0
par = 0
impar = 0
for c in range(10):
    c += 1
    num = int(input(f'{c}º valor: '))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
print(f'-- > Foram digitados {par} números pares e {impar} números ímpares.')
