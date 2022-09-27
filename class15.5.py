print('{:=^50}'.format(' shopee ' ))
somap = total = contagem = menor = 0
barato = ''
while True:
    prod = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    print('='*50)

    contagem += 1
    total += preco
    if preco > 1000:
        somap += 1
    if contagem == 1 or preco < menor:
        menor = preco
        barato = prod
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    print('='*50)

    if continuar == 'S':
        print('{:-^50}'.format(' novo produto ' ))
    if continuar == 'N':
        print('{:-^50}'.format(' fim do programa ' ))
        print('='*50)
        break
    print('='*50)

print(f'O total da compra foi de R${total}.')
print(f'Há {somap} produto(s) custando mais de R$1000.00.')
print(f'O produto mais barato foi a(o) {barato} de R${menor}.')