print('{:^55}'.format('\033[1mCOLEÇÃO DE CDs\033[m'))
print('-'*50)
cds = int(input('* Quantidade de CDs adquiridos: '))
tot_cds = 0
tot_precos = 0
for tot_cds in range(cds):
    tot_cds += 1
    preco = float(input(f'- Preço CD {tot_cds}: R$ '))
    tot_precos += preco
media = tot_precos / tot_cds
print('{:^55}'.format('\033[1mRESULTADO\033[m'))
print('-'*50)
print(f'> Total de CDs colecionados: {tot_cds}')
print(f'> Valor total investido na coleção: R$ {tot_precos:.2f}')
print(f'> Valor médio de cada CD: R$ {media:.2f}')
