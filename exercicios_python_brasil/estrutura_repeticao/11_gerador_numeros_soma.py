print('\033[1m>>> CONTAGEM <<<\033[m')
n1 = int(input('1º VALOR: '))
n2 = int(input('2º VALOR: '))
soma = 0
if n2 > n1 or n1 == n2:
    for c in range(n1 - 1, n2):
        c += 1
        print(c, end=' ')
        soma += c
elif n1 > n2 or n1 == n2:
    for c in range(n2 - 1, n1):
        c += 1
        print(c, end=' ')
        soma += c
print('\nTerminei de contar! =)')
print(f'A soma dos valores é: {soma}!')
