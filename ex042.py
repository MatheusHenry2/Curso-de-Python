list = []
menor = 9999999
posmaior = posmenor = maior = 0
for i in (range(0, 5)):
    list.append((int(input('Informe um valor'))))
    if maior < list[i]:
        maior = list[i]
        posmaior = i + 1
    if list[i] < menor:
        menor = list[i]
        posmenor = i + 1

print(f'O maior valor {maior}\nO menor valor {menor} \nposicao do maior {posmaior} \nposicao do menor {posmenor} ')
for i in range(0, len(list)):
    print(i, end=" ")
