s = 0
for i in range(1, 501):
    if i % 2 != 0 and i % 3 == 0:
        s = s + i
print(f'A soma : {s}')
