print('\033[1mPanificadora - Tabela de Preços\033[m')
preco = float(input('>> Preço do pão: R$ '))
print('\033[1m    QUANTIDADE    |      PREÇO\033[m')
print('¨' * 37)
c = 0
for c in range(9):
    c += 1
    total = c * preco
    print(f'         {c:0>2}       |    R$ {total:.2f}')
    print('¨'*37)
for c in range(10, 50):
    c += 1
    total = c * preco
    print(f'         {c}       |    R$ {total:.2f}')
    print('¨'*37)
