s = 0
velho = ""
underage = 0
maior = 0
for i in range(0, 4):
    nome = str(input('Informe o nome da pessoa:'))
    idade = int(input('Informe a idade da pessoa:'))
    sexo = str(input('Informe o sexo da pessoa'))
    s += idade
    if idade < 20 and sexo == 'feminino' or sexo == 'Feminino':
        underage += 1

    if idade > maior and sexo == 'masculino' or sexo == 'Masculino':
        velho = nome

print(f'A média das idades lidas {(s / 4) :.2f}')
print(f'O nomem do homem mais velho: {velho}')
print(f'O total de mulheres abaixo dos 20 anos: {underage}')
