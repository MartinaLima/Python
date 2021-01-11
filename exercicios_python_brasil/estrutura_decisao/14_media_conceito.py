print('\033[1m>>> MÉDIA ARITMÉTICA <<<\033[m')
n1 = float(input('- 1ª NOTA: '))
n2 = float(input('- 2ª NOTA: '))
media = (n1+n2)/2
print('\033[1mRESULTADO:\033[m')
print(f'MÉDIA: \033[1:33m{media:.2f}\033[m')
if 9 <= media <= 10:
    print('\033[1:32mAPROVADO\033[m\nCONCEITO: A')
elif 7.5 <= media < 9:
    print('\033[1:32mAPROVADO\033[m\nCONCEITO: B')
elif 6 <= media < 7.5:
    print('\033[1:32mAPROVADO\033[m\nCONCEITO: C')
elif 4 <= media < 6:
    print('\033[1:31mREPROVADO\033[m\nCONCEITO: D')
elif 0 <= media < 4:
    print('\033[1:31mREPROVADO\033[m\nCONCEITO: E')
