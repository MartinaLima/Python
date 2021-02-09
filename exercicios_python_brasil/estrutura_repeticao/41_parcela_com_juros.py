print('* CALCULADORA DE PARCELAS *')
divida = float(input('Valor da dívida: R$ '))
print('{:^60}'.format('\033[4mTABELA DE PARCELAMENTO\033[m'))
print('\033[4mVALOR DÍVIDA  |  PARCELAS |    JUROS   | VALOR PARCELA\033[m')
print(f' R$ {divida:.2f}   |    01     |  R$ 0,00   |  R$ {divida:.2f} ')
porcentagem_juros = 5
for parcela in range(2, 12, 3):
    parcela += 1
    porcentagem_juros += 5
    juros = ((divida * porcentagem_juros)/100)
    novo_valor = divida + juros
    valor_parcela = novo_valor/parcela
    if parcela < 12:
        print(f' R$ {novo_valor:.2f}   |    {parcela:0>2}     |  R$ {juros:.2f} |  R$ {valor_parcela:.2f} ')
    else:
        print(f' R$ {novo_valor:.2f}   |    {parcela}     |  R$ {juros:.2f} |  R$ {valor_parcela:.2f} ')
