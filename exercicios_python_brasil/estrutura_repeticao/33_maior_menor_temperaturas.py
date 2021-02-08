print('>>> DEPARTAMENTO ESTADUAL DE METEOROLOGIA <<<')
print('Informe a temperatura ou digite 0 para finalizar!')
c = 0
temp = 1
tot_temp = 0
while temp != 0:
    c += 1
    temp = float(input(f'- Temperatura {c}: '))
    tot_temp += temp
    if c == 1:
        maior = temp
    else:
        if temp > maior:
            maior = temp
    if c == 1:
        menor = temp
    else:
        if temp < menor and temp !=0:
            menor = temp
if tot_temp == 0:
    media = 0
else:
    media = tot_temp / (c-1)
print('Finalizando......................')
print(f'* Maior temperatura: {maior:.2f}')
print(f'* Menor temperatura: {menor:.2f}')
print(f'* Média geral: {media:.2f}')
