nome = str(input('Digite seu nome: ').upper())
senha = (input('Digite a senha: ').upper())
while senha == nome:
    print('A SENHA NÃO PODE SER IGUAL AO NOME! INFORME UMA SENHA VÁLIDA!')
    nome = str(input('Digite seu nome: ').upper())
    senha = (input('Digite a senha: ').upper())
print('SENHA VÁLIDA!')
