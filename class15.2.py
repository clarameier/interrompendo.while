while True:
    print('='*50)
    tabuada = int(input('Digite um número e lhe daremos a sua tabuada: '))
    print('='*50)
    if tabuada < 0:
        break
    for c in range(0, 11):
        print(f'{tabuada} x {c} = {tabuada*c}')
print('PROGRAMA TABUADA ENCERRADO!')
print('='*50)