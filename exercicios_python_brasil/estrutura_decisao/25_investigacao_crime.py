print('\033[1m DEPARTAMENTO DE INVESTIGAÇÃO\033[m')
print('º' * 30)
print('Por favor, responda o questionário abaixo para andamento do processo.')
respostas = [input('- Telefonou para a vítima? [SIM / NÃO]: ').upper(),
             input('- Esteve no local do crime? [SIM / NÃO]: ').upper(),
             input('- Mora perto da vítima? [SIM / NÃO]: ').upper(),
             input('- Possuía dívidas com a vítima? [SIM / NÃO]: ').upper(),
             input('- Trabalhou com a vítima? [SIM / NÃO]: ').upper()]
qnt_sim = respostas.count('SIM')
print('CONSIDERAÇÕES FINAIS:\nO(a) interrogado(a) é considerado(a)', end=' ')
if qnt_sim == 2:
    print('SUSPEITO(A)!')
elif 3 <= qnt_sim <= 4:
    print('CÚMPLICE!')
elif qnt_sim > 4:
    print('ASSASSINO(A)!')
else:
    print('INOCENTE!')
