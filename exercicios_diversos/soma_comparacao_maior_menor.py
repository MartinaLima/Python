print('>>> Informe três valores:')
n1 = int(input('- 1º VALOR: '))
n2 = int(input('- 2º VALOR: '))
n3 = int(input('- 3º VALOR: '))
soma = n1 + n2
if soma > n3:
    resultado = 'MAIOR que o'
elif soma < n3:
    resultado = 'MENOR que o'
else:
    resultado = 'IGUAL ao'
print(f'A soma de {n1} e {n2} é igual a {soma} e é {resultado} terceiro valor {n3}.')
