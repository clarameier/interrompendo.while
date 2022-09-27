from random import randint

print('='*50)
print('Vamos jogar ímpar par!')
print('='*50)

vencer = 0

while True:
#jogador
    jogo = int(input('Digite um número de 1 a 10: '))
#computador
    pc = randint(0, 11)
#soma jogo
    soma = jogo + pc
#PpIi
    Pi = ' '
    while Pi not in 'PI':
        Pi = str(input('Você quer par ou ímpar? [P/I]: ')).strip().upper()[0]
        print('='*50)
#total soma jogo
    print(f'Você jogou {jogo} e o computador {pc}. No total deu {soma}! ', end= '')
    print('Ou seja, deu par!' if soma % 2 == 0 else 'Ou seja, deu ímpar!')
    print('='*50)
#ímpar par
    if Pi == 'P':
        if soma % 2 == 0:
            print('Você ganhou!')
            vencer += 1
        else:
            print('Você perdeu!')
            break
    elif Pi == 'I':
        if soma % 2 == 1:
            print('Você ganhou!')
            vencer += 1
        else:
            print('Você perdeu!')
            break
    print('='*50)
    print('Vamos para o próximo round!')
print(f'Você venceu {vencer} vezes.')
