lista = [[], []]
for i in range(0, 7):
    n = int(input('Valor :'))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print(f'A lista com pares : {lista[0]}')
print(f'A lista com impares : {lista[1]}')