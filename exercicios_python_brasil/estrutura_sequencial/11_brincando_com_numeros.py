from math import pow
n1 = int(input('> Por favor, informe um número inteiro (sem vírgula): '))
n2 = int(input('> Informe outro número inteiro: '))
n3 = float(input('> Agora informe um número real (com vírgula): '))
r1 = (n1*2)*(n2/2)
r2 = (n1*3)+n3
r3 = pow(n3, 3)
print('-'*40)
print('\033[1m>>> RESULTADOS <<<\033[m')
print(f'O produto do dobro de {n1} com metade de {n2}: \033[1m{r1:.2f}\033[m')
print(f'A soma do triplo de {n1} com {n3}: \033[1m{r2:.2f}\033[m')
print(f'{n3} elevado ao cubo: \033[1m{r3:.2f}')
