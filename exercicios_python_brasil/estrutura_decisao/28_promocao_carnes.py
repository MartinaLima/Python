print('{:^55}'.format('\033[1m>>> HIPERMERCADOS TABAJARA <<<\033[m'))
print('ESCOLHA O PRODUTO:')
opcao = int(input('[1] Filé duplo\n[2] Alcatra\n[3] Picanha\n---> '))
if opcao in [1, 2, 3]:
    quantidade = float(input('INFORME A QUANTIDADE: Kg '))
    if opcao == 1:
        produto = 'FILÉ DUPLO'
        if quantidade <= 5:
            preco = quantidade * 4.90
        else:
            preco = quantidade * 5.80
    elif opcao == 2:
        produto = 'ALCATRA'
        if quantidade <= 5:
            preco = quantidade * 5.90
        else:
            preco = quantidade * 6.80
    else:
        produto = 'PICANHA'
        if quantidade <= 5:
            preco = quantidade * 6.90
        else:
            preco = quantidade * 7.80
    cartao = str(input('DESEJA PAGAR COM CARTÃO TABAJARA? [SIM/ NÃO] ').upper())
    if cartao in 'SSIM':
        desconto = ((preco * 5) / 100)
        preco_final = preco - ((preco * 5) / 100)
        pagamento = 'SIM'
    else:
        desconto = 0
        preco_final = preco
        pagamento = 'NÃO'
    print('-' * 50)
    print('{:^55}'.format('\033[1mRESUMO DA COMPRA\033[m'))
    print(f'- PRODUTO: {produto}')
    print(f'- QUANTIDADE: {quantidade} Kg')
    print(f'- PREÇO TOTAL: R$ {preco:.2f}')
    print(f'- PAGAMENTO COM CARTÃO DA LOJA? {pagamento}')
    print(f'- DESCONTO: R$ {desconto:.2f}')
    print(f'- PREÇO FINAL A PAGAR: R$ {preco_final:.2f}')
else:
    print('OPÇÃO INVÁLIDA!')
