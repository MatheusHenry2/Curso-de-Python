n = s = d = 0
while n != 999:
    n = int(input('Informe um número'))
    if n != 999:
        s += n
        d += 1
print(f'O total de números digitados: {d} a soma {s} ')

