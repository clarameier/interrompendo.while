#while contagem
print('='*100)
contagem = 1
while contagem <= 10:
    print(contagem, '-> ', end='')
    contagem += 1
print('fim.')

#while numero
print('='*100)
numero = 0
soma = 0
while numero != 999: #ao digitar 999 trava o looping
    numero = int(input('Digite um número inteiro (digite 999 para parar o programa): '))
    soma += numero
soma -= 999 #retira da soma os 999 que trava o looping
print('A soma dos números digitados vale {}.'.format(soma))

#while true
print('='*100)
numero = soma = 0
while True:
    numero = int(input('Digite um número inteiro (digite 999 para parar o programa): '))
    if numero == 999:
        break
    soma += numero
print('A soma dos números digitados vale {}.'.format(soma))

#while true
print('='*100)
numero = soma = 0
while True:
    numero = int(input('Digite um número inteiro (digite 999 para parar o programa): '))
    if numero == 999:
        break
    soma += numero
print(f'A soma dos números digitados vale {soma}.') #ao inves de format, usar f

#teste do format, f, %
nome = 'Maria'
idade = 19
salario = 3000.00
print(f'A {nome} tem {idade} anos e ganha R${salario:.2f}.')
print('A {} tem {} anos.'.format(nome, idade))
print('A %s tem %d anos.' % (nome, idade))

