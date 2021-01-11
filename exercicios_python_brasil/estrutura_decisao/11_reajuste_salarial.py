print('\033[1m>>> REAJUSTE SALARIAL <<<\033[m')
nome = str(input('NOME FUNCIONÁRIO(A): '))
salario = float(input('SALÁRIO ATUAL: R$ '))
if salario <= 280:
    aumento = (salario*20)/100
    novo_sal = salario+aumento
    perc = 20
elif 280 < salario <= 700:
    aumento = (salario*15)/100
    novo_sal = salario+aumento
    perc = 15
elif 700 < salario <= 1500:
    aumento = (salario*10)/100
    novo_sal = salario+aumento
    perc = 10
else:
    aumento = (salario*5)/100
    novo_sal = salario+aumento
    perc = 5
print('\033[1mRESULTADO\033[m')
print(f'> FUNCIONÁRIO(A): {nome.upper()}')
print(f'> SALÁRIO ATUAL: R$ {salario:.2f}')
print(f'> REAJUSTE: {perc}%')
print(f'> VALOR DO REAJUSTE: R$ {aumento:.2f}')
print(f'> NOVO SALÁRIO: R$ {novo_sal:.2f}')
