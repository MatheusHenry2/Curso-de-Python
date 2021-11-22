try:
    valor = int(input('Informe o valor :'))
    n = int(input('Informe uma opcao de 0 a 3'))
    if n == 1:
        print(f'o valor {valor} em bi', bin(valor))
    elif n == 2:
        print(f'o valor {valor} em octal', oct(valor))
    elif n == 3:
        print(f'o valor {valor} em bi', hex(valor))
    else:
        print('Valor inválido')
except:
    print('Caracter inválido')






