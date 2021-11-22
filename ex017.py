n = int(input('Informe um numero :'))
primo = 0

for i in range(1, n + 1):
    if n % i == 0:
        primo = primo + 1

print(f'Total divisores {primo}')

if primo <= 2:
    print(f'O número {n} é primo ')
else:
    print(f'O número  {n} não é primo ')
