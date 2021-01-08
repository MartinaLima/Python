print('\033[1m>>> CALCULADORA DE TINTAS - LOJA ABC <<<\033[m')
area = float(input('ÁREA A SER PINTADA (m²): '))
litros = (area/3)
lata = (litros/18)
preco = lata*80
print('-'*40)
print(f'QUANTIDADE NECESSÁRIA: {litros:.2f} litro(s)')
print(f'LATA (18 LITROS): {lata:.2f} lata(s).')
print(f'VALOR TOTAL: R$ {preco:.2f}')
