print('---Menu de escolhas---')
print('---1 Para somar---')
print('---2 Para multiplicar---')
print('---3 Para achar o maior ---')
print('---4 Para novos números  ---')
opcao = 30
valor1 = float(input('Informe o número:'))
valor2 = float(input('Informe outro número'))

while opcao != 5:
    opcao = int(input('Informe a opcao:'))
    if opcao == 1:
        print(f'Soma: {valor1 + valor2 :.2f}')
    elif opcao == 2:
        print(f'Multiplicação : {valor1 * valor2 :.2f}')
    elif opcao == 3:
        if valor1 > valor2:
            print(f'o maior valor é {valor1}')
        else:
            print(f'O maior valor é {valor2}')
    else:
        valor1 = float(input('Informe o número:'))
        valor2 = float(input('Informe outro número'))
        opcao = int(input('Informe a opcao:'))
print('fim')
