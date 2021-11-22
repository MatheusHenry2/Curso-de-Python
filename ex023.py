import random
pal = 0
game = 6
n = 7

while game != n:
    game = int(input('Informe um número de 0 a 10'))
    n = random.randint(0, 10)
    print(f'O número escolhido pelo computador {n} por Você {game}')
    pal += 1
print(f'O total de paplites {pal}')
