ans = ''
up = men = wom = 0
while True:
    idade = int(input('Informe sua idade:'))
    sexo = str(input('Informe seu sexo M ou F').strip().upper()[0])
    if idade > 18:
        up += 1
    if sexo == 'M':
        men += 1
    if sexo == 'F' and idade < 20:
        wom += 1
    ans = str(input('Quer continuar S ou N :').strip().upper()[0])
    if ans == 'N':
        break
print(f'O total de pessoas com mais de 18: {up}')
print(f'O total de homens cadastrados: {men}')
print(f'O total de mulheres abaixo dos 20: {wom}')
