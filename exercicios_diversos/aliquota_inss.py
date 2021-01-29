"""Crie um programa que leia o nome completo de um funcionário e seu salário bruto e com base nisso,
calcule a alíquota a ser descontada pelo INSS. Ao final informe o nome do funcionário, o salário bruto,
a qual porcentagem de alíquota se encaixa, o valor total descontado pelo INSS e o valor líquido (a receber).
Considere a seguinte tabela de alíquota do INSS. 
Até R$ 1751.81 - ALÍQUOTA DE 8% 
De R$ 1751,82 até R$ 2919.72 - ALÍQUOTA DE 9% 
De R$ 2919.73 até R$ 5839.44 - ALÍQUOTA DE 11% 
A partir de R$ 5839.45 - ALÍQUOTA R$ 642,38 """

print('-'*12 + ' DESCONTO INSS ' + '-'*11)
nome = str(input('NOME FUNCIONÁRIO(A): '))
bruto = float(input('SALÁRIO BRUTO: R$ '))
if bruto <= 1751.81:
    aliquota = '8%'
    inss = (bruto * 8) / 100
elif 1751.82 < bruto <= 2919.72:
    aliquota = '9%'
    inss = (bruto * 9) / 100
elif 2919.72 < bruto <= 5839.44:
    aliquota = '11%'
    inss = (bruto * 11) / 100
else:
    aliquota = 'R$ 642,38'
    inss = 642.38
print('-'*15 + ' TOTAIS ' + '-'*15)
print(f'- FUNCIONÁRIO(A): {nome}'.upper())
print(f'- SALÁRIO BRUTO: R$ {bruto:.2f}')
print(f'- ALÍQUOTA INSS: {aliquota}')
print(f'- DESCONTO INSS: R$ {inss:.2f}')
print(f'- VALOR LÍQUIDO (A RECEBER): R$ {bruto - inss:.2f}')
