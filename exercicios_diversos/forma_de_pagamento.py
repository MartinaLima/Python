print('*'*15 + ' PAGAMENTO ' + '*'*15)
valor = float(input('VALOR DA COMPRA: R$ '))
pagamento = 0
while pagamento not in (1, 2, 3, 4):
    pagamento = int(input('FORMA DE PAGAMENTO:\n'
                          '[1] À VISTA - 10% (DINHEIRO OU CHEQUE)\n'
                          '[2] À VISTA - 15% (CARTÃO DE CRÉDITO)\n'
                          '[3] PARCELADO EM 2X\n'
                          '[4] PARCELADO EM 3X + 10% juros\n'
                          '=> '))
    if pagamento in (1, 2, 3, 4):
        if pagamento == 1:
            total = valor - ((valor * 10)/100)
        elif pagamento == 2:
            total = valor - ((valor * 15)/100)
        elif pagamento == 3:
            total = valor
        else:
            total = valor + ((valor * 10)/100)
        print('*' * 17 + ' TOTAL ' + '*' * 17)
        print(f'- VALOR INICIAL: R$ {valor:.2f}')
        print(f'- VALOR A PAGAR: R$ {total:.2f}')
    else:
        print('OPÇÃO INVÁLIDA!')
