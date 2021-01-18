num = int(input('Digite uma nota de 0 à 10: '))
while num < 0 or num > 10:
    print('NOTA INVÁLIDA!')
    num = int(input('Digite uma nota de 0 à 10: '))
print('NOTA VÁLIDA!')
