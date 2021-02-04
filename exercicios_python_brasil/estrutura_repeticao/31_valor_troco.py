while True:
    print('{:^55}'.format('LOJAS TABAJARA - CADASTRO NOVA COMPRA'))
    print('¨' * 55)
    print('* Informe o valor do produto ou 0 para finalizar!')
    preco = 1
    c = 0
    preco_total = preco - 1
    while preco != 0:
        c += 1
        preco = float(input(f'Produto {c}: R$ '))
        while preco < 0:
            preco = float(input(f'Produto {c}: R$ '))
        preco_total += preco
    print('\033[1m>>> TOTAL DA COMPRA\033[m')
    print(f'* Quantidade itens: {c - 1}')
    print(f'* Preço total: R$ {preco_total:.2f}')
    pago = float(input('* Valor pago: R$ '))
    if pago >= preco_total:
        troco = pago - preco_total
        print(f'* Troco: R$ {troco:.2f}')
    else:
        troco = preco_total - pago
        print(f'* Saldo Devedor: R$ {troco:.2f}')
    print('Finalizando '+'.'*43)
