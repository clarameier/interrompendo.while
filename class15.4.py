print('='*50)
print('Cadastre o indivíduo aqui')
print('='*50)

dezoito = homens = mulheres = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print('='*50)
    if idade >= 18:
        dezoito += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1

    novo = ' '
    while novo not in 'SN':
        novo = str(input('Deseja cadastrar outra pessoa? [S/N]: ')).strip().upper()[0]
    print('='*50)

    if novo == 'S':
        print('----- Novo cadastro -----')
    if novo == 'N':
        print('Obrigada pela participação!')
        print('='*50)
        break
    print('='*50)    
print(f'Total de cadastro de pessoas com mais de 18 anos: {dezoito}.')
print(f'Ao todo {homens} homens foram cadastrados.')
print(f'E {mulheres} mulheres com menos de 20 anos foram cadastradas.')
print('='*50)