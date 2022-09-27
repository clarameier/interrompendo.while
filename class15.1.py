numero = 0
soma = 0
contagem = 0
while True:
    numero = int(input('Digite um número inteiro (digite 999 para interromper o programa): '))
    if numero == 999:
        break
    soma += numero
    contagem += 1
print(f'Você digitou {contagem} números e a soma deles foi de {soma}')