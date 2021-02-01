print('-'*9 + ' FOLHA DE PAGAMENTO ' + '-'*9)
nome = str(input('NOME FUNCIONÁRIO(A): '))
bruto = float(input('SALÁRIO BRUTO: R$ '))
bonus = (bruto * 20) / 100
novo_salario = bruto + bonus
inss = (novo_salario * 10) / 100
salario_sem_inss = novo_salario - inss
ir = (salario_sem_inss * 30) / 100
liquido = salario_sem_inss - ir
print('-'*15 + ' TOTAIS ' + '-'*15)
print(f'- FUNCIONÁRIO(A): {nome}'.upper())
print(f'- SALÁRIO BRUTO: R$ {bruto:.2f}')
print(f'- BÔNUS: R$ {bonus:.2f}')
print(f'- INSS (10%): R$ {inss:.2f}')
print(f'- IR (30%): R$ {ir:.2f}')
print(f'- TOTAL DESCONTOS: R$ {inss+ir:.2f}')
print(f'- TOTAL A RECEBER: R$ {liquido:.2f}')
