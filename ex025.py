n = int(input('Informe o número para seu fatorial:'))
fat = 1

for i in range(1, n + 1):
    print(f'x {i}', end=" ")
    fat = fat * i
print(f'O FATORIAL: {fat} ')
