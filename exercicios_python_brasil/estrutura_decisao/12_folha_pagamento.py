print('\033[1m>>> FOLHA DE PAGAMENTO <<<\033[m')
v_hora = float(input('VALOR HORA: R$ '))
horas = int(input('HORAS TRABALHADAS NO MÊS: '))
bruto = v_hora*horas
if bruto <= 900:
    ir = 0
    porc = 0
elif 900 < bruto <= 1500:
    ir = (bruto*5)/100
    porc = 5
elif 1500 < bruto <= 2500:
    ir = (bruto*10)/100
    porc = 10
else:
    ir = (bruto*20)/100
    porc = 20
inss = (bruto*10)/100
sindicato = (bruto*3)/100
fgts = (bruto*11)/100
total_desc = (ir+inss+sindicato)
liquido = bruto-(ir+inss+sindicato)
print('\033[1mTOTAIS:\033[m')
print(f'SALÁRIO BRUTO:................. R$ {bruto:.2f}')
print(f'IR ({porc}%):....................... R$ {ir:.2f}')
print(f'INSS (10%):.................... R$ {inss:.2f}')
print(f'SINDICATO (3%):................ R$ {sindicato:.2f}')
print(f'VALOR FGTS (11%):.............. R$ {fgts:.2f}')
print(f'TOTAL DESCONTOS:............... R$ {total_desc:.2f}')
print(f'SALÁRIO LÍQUIDO:............... R$ {liquido:.2f}')
