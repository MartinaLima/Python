from time import sleep
print('Contando números ímpares de 1 até 50...')
for c in range(0, 50, 2):
    sleep(0.3)
    c += 1
    print(c, end=' ')
print('\nTerminei de contar! =)')

