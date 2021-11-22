preco = float(input('Informe o preço do produto:'))
opcao = int(input('Informe a opcao de pagamento: 1 a 4'))

if opcao == 1:
    print(f'O valor do produto é {preco} o desconto é {preco * 0.10} e o preco com desconto: {preco - (preco * 0.10)}')
elif opcao == 2:
    print(f'O valor do produto é {preco} o desconto é {preco * 0.05} e o preco com desconto: {preco - (preco * 0.05)}')
elif opcao == 3:
    print(f'O valor do produto {preco}')
elif opcao == 4:
     parcela = int(input('Informe quantas paracelas serao'))
     valor = (preco/parcela)
     print(f'O valor do parcela é {valor} o juros é {valor * 0.20} e o preco com juros: {(valor) + (valor * 0.20)}')



