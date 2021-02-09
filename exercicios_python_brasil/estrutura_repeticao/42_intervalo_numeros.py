print('>> Informe valores, ou um valor negativo para finalizar!')
c = 0
int_a = 0
int_b = 0
int_c = 0
int_d = 0
while True:
    c += 1
    num = int(input(f'{c}º Valor: '))
    if num < 0:
        break
    if 0 <= num <= 25:
        int_a += 1
    elif 26 <= num <= 50:
        int_b += 1
    elif 51 <= num <= 75:
        int_c += 1
    elif 76 <= num <= 100:
        int_d += 1
print('-'*40)
print(f'NÚMEROS INFORMADOS: {c-1}')
print(f'* Números intervalo [ 0 -  25]: {int_a}')
print(f'* Números intervalo [26 -  50]: {int_b}')
print(f'* Números intervalo [51 -  75]: {int_c}')
print(f'* Números intervalo [76 - 100]: {int_d}')
