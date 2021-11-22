import random
print('1 tesoura, 2 pedra, 3 papel')
valor = int(input('Informe sua jogada:'))
robo = random.randint(1,4)


if valor == robo:
    print('Empate')
elif valor == 1 and robo == 2:
    print('Robo venceu')
elif valor == 2 and robo == 3:
    print('Robo venceu')
elif valor == 3 and robo == 1:
    print('Robo venceu')
if robo == 1 and valor == 2:
    print('Humano venceu')
elif robo == 2 and valor == 3:
    print('Humano venceu')
elif robo == 3 and valor == 1:
    print('Humano venceu')