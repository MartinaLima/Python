print('>>> Informe um número para calcular seu fatorial!')
num = int(input('- Número: '))
while num < 0:
    print('Digite um valor positivo!')
    num = int(input('- Número: '))
fatorial = 1
for c in range(num, 0, -1):
    fatorial *= c
    if c == 1:
        print(c)
    else:
        print(f'{c} ', end='x ')
print(f'* Fatorial de {num}: {fatorial}')
