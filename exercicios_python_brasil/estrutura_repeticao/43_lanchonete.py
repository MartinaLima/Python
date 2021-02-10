print('{:^40}'.format('CARDÁPIO - LANCHONETE ALEGRIA VEGGIE'))
print('º'*40)
print('\033[4m      LANCHE       | CÓDIGO  |   PREÇO  \033[m\n'
      ' "Not" Dog         |   100   |  R$ 1,20\n'
      ' Combo Simples     |   101   |  R$ 1,30\n'
      ' Combo Especial    |   102   |  R$ 1,50\n'
      ' Hambúrguer Veggie |   103   |  R$ 1,20\n'
      ' Pizza Veggie      |   104   |  R$ 1,30\n'
      ' Refrigerante      |   105   |  R$ 1,00')
print('º'*40)
total_pedido = 0
todos = 0
itens = list()
while True:
    opcao = int(input('Código do lanche: '))
    while opcao not in (100, 101, 102, 103, 104, 105):
        print('CÓDIGO INVÁLIDO!')
        opcao = int(input('Código do lanche: '))
    qnt = int(input('Quantidade: '))
    print('-'*30)
    if opcao == 100:
        preco = 1.20 * qnt
        lanche = '"Not" Dog'
    elif opcao == 101:
        preco = 1.30 * qnt
        lanche = 'Combo Simples'
    elif opcao == 102:
        preco = 1.50 * qnt
        lanche = 'Combo Especial'
    elif opcao == 103:
        preco = 1.20 * qnt
        lanche = 'Hambúrguer Veggie'
    elif opcao == 104:
        preco = 1.30 * qnt
        lanche = 'Pizza Veggie'
    else:
        preco = 1.00 * qnt
        lanche = 'Refrigerante'
    total_pedido += preco
    itens.append(lanche)
    fim = str(input('Finalizar pedido? [S/N] ').upper())
    if fim == 'S':
        print('Finalizando...')
        break
    while fim not in 'SN':
        fim = str(input('Finalizar pedido? [S/N] ').upper())
print('{:^40}'.format('TOTAL PEDIDO'))
print('º'*40)
print('Itens:')
for c in range(len(itens)):
    print('- ', itens[c])
print(f'TOTAL A PAGAR: R$ {total_pedido:.2f}')
