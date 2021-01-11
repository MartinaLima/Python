print('>>> Informe uma letra e direi se é vogal ou consoante!')
letra = str(input('-> ').upper())
primeira = letra[0]  # Mesmo que o entrada possua mais de um caractere, será considerado somente o primeiro.
if primeira in 'AEIOU':
    print(f'A letra {primeira} é uma \033[1mVOGAL\033[m! :)')
elif primeira in 'BCDFGHJKLMNPQRSTVXWYZ':
    print(f'\033[1mA letra {primeira} é uma \033[1mCONSOANTE\033[m! :D')
else:
    print('Não consegui adivinhar! :(')
