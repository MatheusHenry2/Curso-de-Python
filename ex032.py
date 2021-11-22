import random

while True:
    valor = str(input('Você quer P ou I').upper())
    n = int(input('Informe o valor 0 a 10'))
    computador = random.randint(0, 11)

    if valor == 'P':
        if (n + computador) % 2 == 0:
            print(f'you {n} PC {computador} deu {n + computador} Vitoria!!')
        else:
            print(f'you {n} PC {computador} deu {n + computador} Perdeu!!')
            break
    if valor == 'I':
        if (n + computador) % 2 != 0:
            print(f'you {n} PC {computador} deu {n + computador} Vitoria!!')
        else:
            print(f'you {n} PC {computador} deu {n + computador} Perdeu!!')
            break
