print('EM QUE TURNO VOCÊ ESTUDA?\n[M] Matutino\n[V] Vespertino\n[N] Noturno')
turno = str(input('>>> ').upper())
if turno in 'M' or turno in 'MATUTINO':
    print('Então... BOM DIA! =D')
elif turno in 'V' or turno in 'VESPERTINO':
    print('Então... BOA TARDE! =D')
elif turno in 'N' or turno in 'NOTURNO':
    print('Então... BOA NOITE! =D')
else:
    print('Não reconheci o turno! =(')
