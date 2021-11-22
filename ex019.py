maiores = 0

for i in range(0, 7):
    ano = int(input('Informe o ano:'))
    if 2021 - ano >= 21:
        maiores += 1

print(f'A quantidade de maiores idade {maiores}')
print(f'A quantidade dde menores de idade{7-maiores}')
