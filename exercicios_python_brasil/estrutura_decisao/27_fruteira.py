print('\033[1m>>> FRUTEIRA TENDA DAS FRUTAS <<<\033[m')
print('INFORME O PESO (Kg) DOS PRODUTOS:')
peso_morango = float(input('- MORANGO: Kg '))
peso_maca = float(input('- MAÇÃ: Kg '))
print('-'*35)
if peso_morango <= 5:
    preco_morango = peso_morango*2.50
else:
    preco_morango = peso_morango*2.20
if peso_maca <= 5:
    preco_maca = peso_maca*1.80
else:
    preco_maca = peso_maca*1.50
peso_total = peso_maca+peso_morango
preco_total = preco_maca+preco_morango
if peso_total > 8 or preco_total > 25.00:
    preco_total = preco_total-((preco_total*10)/100)
    print('DESCONTO DE 10%!')
print(f'\033[1mTOTAL A PAGAR:\033[m R$ {preco_total:.2f}')
