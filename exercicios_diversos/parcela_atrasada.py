print('\033[1m>>> CALCULADORA DE JUROS <<<\033[m')
parcela = float(input('- VALOR DA PARCELA: R$ '))
dias = int(input('- DIAS DE ATRASO: '))
juros = float(input('- JUROS AO DIA: '))
acrescimo = ((juros*dias) * parcela) / 100
total = parcela + acrescimo
print('\033[1mRESULTADO:\033[m\n'
      f'ACRÉSCIMO: R$ {acrescimo:.2f}\n'
      f'ATRASO: {dias} dias\n'
      f'TOTAL A PAGAR: R$ {total:.2f}')
