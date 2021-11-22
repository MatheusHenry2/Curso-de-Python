casa = float(input('Informe o valor da casa :'))
salario = float(input('Informe o valor do salário'))
anos = int(input('Informe quantos anos você vai pagar'))

p = (casa / (anos * 12))

if p > salario * 0.30:
    print('Emprestimo negado')
else:
    print('Emprestimo concedido')























