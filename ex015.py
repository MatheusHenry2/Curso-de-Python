s = 0
for i in range(0, 6):
    n = int(input('Informe um numero:'))
    if n % 2 == 0:
        s = s + n
print(f'A Soma dos pares : {s}')
