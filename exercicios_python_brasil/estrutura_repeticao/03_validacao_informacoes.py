nome = str(input('Informe o nome: '))
nome = ''.join(nome.split())
while len(nome) < 3:
    print('O nome deve ter ao menos 3 letras!')
    nome = str(input('Informe o nome: '))
    nome = ''.join(nome.split())

idade = int(input('Informe a idade: '))
while idade < 0 or idade > 150:
    print('IDADE INVÁLIDA!')
    idade = int(input('Informe a idade: '))

salario = float(input('Informe o salário: R$ '))
while salario <= 0:
    print('SALÁRIO INVÁLIDO!')
    salario = float(input('Informe o salário: R$ '))

sexo = str(input('Informe o sexo [F / M] ').upper())
if len(sexo) > 1:
    while len(sexo) > 1 or sexo not in 'FM':
        print('SEXO INVÁLIDO!')
        sexo = str(input('Informe o sexo [F / M] ').upper())

estado = str(input('Informe o estado civil:'
                   '\n[S] Solteiro(a)'
                   '\n[C] Casado(a)'
                   '\n[V] Viúvo(a)'
                   '\n[D] Divorciado(a)'
                   '\n---> ').upper())
if len(estado) > 1:
    while len(estado) > 1 or estado not in 'SCVD':
        print('ESTADO CIVIL INVÁLIDO!')
        estado = str(input('Informe o estado civil:'
                           '\n[S] Solteiro(a)'
                           '\n[C] Casado(a)'
                           '\n[V] Viúvo(a)'
                           '\n[D] Divorciado(a)'
                           '\n---> ').upper())

print('INFORMAÇÕES REGISTRADAS COM SUCESSO!')
