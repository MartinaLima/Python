print('\033[1m>>> DESCOBRINDO O MAIOR VALOR <<<\033[m')
maior = 0
c = 0
for c in range(5):
    c += 1
    num = int(input(f'- {c}º valor: '))
    if num > maior:
        maior = num
print(f'\nO maior valor encontrado foi \033[1m{maior}\033[1m!')
