lista = []
while True:
    lista.append(int(input('Informe o valor N:')))
    stop = str(input('Quer continuar?').strip().upper()[0])
    if stop == 'N':
        break
print(f'O total de números digitados : {(len(lista))}')
lista.sort(reverse=True)
print(f'A lista me ordem decrescente : {lista}')
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('Não está na lista o valor 5')