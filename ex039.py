v1 = int(input('Informe um valor:'))
v2 = int(input('Informe um valor:'))
v3 = int(input('Informe um valor:'))
v4 = int(input('Informe um valor:'))
num = (v1, v2, v3, v4)
print(f'O total de vezes que apareceu o 9: {(num.count(9))}')
print(f'a posicao que encontrou o valor 3 foi {num.index(3)}')

for i in range(0, len(num)):
    if num[i] % 2 == 0:
        print(f'Os números pares foram : {num[i]}')
