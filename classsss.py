frase = str(input('Digite uma frase: '))
vogal = frase[0]
if vogal in 'aeiou':
    print(f'a primeira vogal é {vogal}.')
else:
    print('não é vogal')