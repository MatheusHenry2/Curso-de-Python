maior = soma = c = 0
menor = 999999
ans = ''

while ans != 'N':
    n = int(input('Informe um valor:'))
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    soma += n
    c += 1
    ans = str(input('Quer continuar S ou N').upper())
print(f'O Maior número {maior}')
print(f'O Menor número {menor}')
print(f'A Média dos valores {(soma / c) :.2f}')
