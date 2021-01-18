print('\033[1m>>> CRESCIMENTO POPULACIONAL <<<\033[m')
hab_a = 80000
hab_b = 200000
ano = 0
while hab_a < hab_b:
    hab_a = hab_a + (hab_a*3)/100
    hab_b = hab_b + (hab_b * 1.5) / 100
    ano += 1
print(f'Serão necessários \033[1m{ano} anos\033[m para que o país A ultrapasse o país B.')
print(f'HABITANTES A (crescimento em 3% ao ano): {hab_a:.0f}')
print(f'HABITANTES B (crescimento em 1.5% ao ano): {hab_b:.0f}')
