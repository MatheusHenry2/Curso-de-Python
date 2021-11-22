lista = []
lista2 = []
lista3 = []
for i in range(0, 10):
    n = int(input('Informe um valor N:'))
    lista.append(n)
    if n % 2 == 0:
        lista2.append(n)
    else:
        lista3.append(n)
print(f'A 1 lista gerada foi : {lista}')
print(f'A 2 lista gerada foi : {lista2}')
print(f'A 3 lista gerada foi : {lista3}')
