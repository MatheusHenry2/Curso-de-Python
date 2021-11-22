lista = []
for i in range(0, 6):
    n = int(input('Informe um número'))
    if n not in lista:
        lista.append(n)
lista.sort()
print(f'A LISTA É {lista}')