ano = int(input('Informe o ano do seu nascimento :'))

if 2021 - ano < 9:
    print('MIRIM')
elif 2021 - ano <= 14:
    print('Infantil')
elif 2021 - ano <= 19:
    print('Junior')
elif 2021 - ano <= 25:
    print('Senior')
else:
    print('Master')