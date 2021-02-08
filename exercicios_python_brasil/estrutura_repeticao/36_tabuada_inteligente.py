print('\033[1m>> TABUADA INTELIGENTE <<\033[m')
base = int(input('* Tabuada de: '))
inicio = int(input('* Inicia em: '))
final = int(input('* Finaliza em: '))
while inicio > final:
    print('O inicio deve ser menor que o final!')
    inicio = int(input('* Inicia em: '))
    final = int(input('* Finaliza em: '))
c = 0
print('-'*25)
print('{:^31}'.format(f'\033[1mTABUADA DO {base}\033[m'))
print('-'*25)
for c in range(inicio - 1, final):
    c += 1
    multi = base * c
    if c >= 0 or c <= 9:
        print(f'      {c:0>2} X {base} = {multi}')
    else:
        print(f'      {c} X {base} = {multi}')
print('-'*25)
