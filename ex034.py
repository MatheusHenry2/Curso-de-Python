total = plow = 0
menor = 9999999
caro = ""
while True:
    nome = str(input('Informe o nome do produto:'))
    preco = float(input('Informe o preço do produto:'))
    total = total + preco

    if preco > 1000:
        plow = plow + 1

    if preco < menor:
        menor = preco
        caro = nome

    ans = str(input('Quer continuar cadastrando S ou N:').strip().upper()[0])
    if ans == 'N':
        break

print(f'O Total gasto na compra {total :2.f}')
print(f'O total de produtos que custam mais que 1000 :{plow}')
print(f'O Nome do produto mais caro : {caro}')
