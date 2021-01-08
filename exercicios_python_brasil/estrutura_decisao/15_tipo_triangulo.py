print('\033[1:33m>>> TIPO DE TRIÂNGULO <<<\033[m')
l1 = int(input('> Digite o 1º lado: '))
l2 = int(input('> Digite o 2º lado: '))
l3 = int(input('> Digite o 3º lado: '))
if l1 == 0 or l2 == 0 or l3 == 0:
    print('Os lados informados \033[31mNÃO \033[mformam triângulo!')
    print('Para que seja possível, nenhum dos lados pode ser igual a ZERO!')
elif l1 >= l2+l3 or l2 >= l1+l3 or l3 >= l2+l1:
    print('Os lados informados \033[31mNÃO \033[mformam triângulo!')
    print('Para que seja possível, a soma de dois lados não pode ser menor ou igual ao 3º lado!')
elif l1 < l2+l3 or l2 < l1+l3 or l3 < l2+l1:
    if l1 == l2 == l3:
        print('Os lados formam um triângulo \033[33mEQUILÁTERO\033[m!')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Os lados formam um triângulo \033[33mISÓSCELES\033[m!')
    else:
        print('Os lados formam um triângulo \033[33mESCALENO\033[m!')
