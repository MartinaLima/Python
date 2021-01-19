print('\033[1m>>> CRESCIMENTO POPULACIONAL <<<\033[m')
print('Preencha com as informações solicitadas abaixo:')
hab_a = int(input('População do país A: '))
while hab_a <= 0:
    print('Número de habitantes inválido!')
    hab_a = int(input('População do país A: '))
taxa_a = float(input('Taxa de crescimento anual do país A: '))
while taxa_a <= 0:
    print('Taxa de crescimento inválida!')
    taxa_a = float(input('Taxa de crescimento anual do país A: '))
hab_b = int(input('População do país B: '))
while hab_b <= 0:
    print('Número de habitantes inválido!')
    hab_b = int(input('População do país B: '))
taxa_b = float(input('Taxa de crescimento anual do país B: '))
while taxa_b <= 0:
    print('Taxa de crescimento inválida!')
    taxa_b = float(input('Taxa de crescimento anual do país B: '))
ano = 0
while hab_a < hab_b:
    hab_a = hab_a + (hab_a*taxa_a)/100
    hab_b = hab_b + (hab_b * taxa_b) / 100
    ano += 1
print('\033[1mRESULTADO...\033[m')
print(f'Serão necessários \033[1m{ano} anos\033[m para que o país A ultrapasse o país B.')
print(f'HABITANTES A (crescimento {taxa_a}% ao ano): {hab_a:.0f}')
print(f'HABITANTES B (crescimento {taxa_b}% ao ano): {hab_b:.0f}')
