saque = int(input('informe o valor :'))
print(f'O total de {saque // 50} cedulas de 50 R$')
print(f'O total de {saque % 50 // 20} cedulas de 20 R$')
print(f'O total de {saque % 50 % 20 // 10} cedulas de 10 R$')
print(f'O total de {saque % 50 % 20 % 10 // 1} cedulas de 1 R$')