from time import sleep
print('\033[1m>>> CONTAGEM DECRESCENTE <<< \033[0m')
n1 = int(input('VALOR 1: '))
n2 = int(input('VALOR 2: '))
n3 = int(input('VALOR 3: '))
print('Contando...')
sleep(1)
if n1 >= n2 and n2 >= n3:
    print(f'{n1}... {n2}... {n3}...')
elif n1 >= n3 and n3 >= n2:
    print(f'{n1}... {n3}... {n2}...')
elif n2 >= n1 and n1 >= n3:
    print(f'{n2}... {n1}... {n3}...')
elif n2 >= n3 and n3 >= n1:
    print(f'{n2}... {n3}... {n1}...')
elif n3 >= n1 and n1 >= n2:
    print(f'{n3}... {n1}... {n2}...')
elif n3 >= n2 and n2 >= n1:
    print(f'{n3}... {n2}... {n1}...')
