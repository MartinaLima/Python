print('\033[1m Lojas Quase Dois - Tabela de Preços\033[m')
print('¨' * 37)
print('\033[1m    QUANTIDADE    |      PREÇO\033[m')
print('¨' * 37)
c = 0
for c in range(9):
    c += 1
    preco = c * 1.99
    print(f'         {c:0>2}       |    R$ {preco:.2f}')
    print('¨'*37)
for c in range(10, 50):
    c += 1
    preco = c * 1.99
    print(f'         {c}       |    R$ {preco:.2f}')
    print('¨'*37)
