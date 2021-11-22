pessoas = list()
dados = list()
totalpessoas = maior = 0
menor = 999999
leves = list()
pesadas = list()
while True:
    dados.append(str(input('Nome :')))
    dados.append(float(input('Peso :')))
    pessoas.append(dados[:])
    leave = str(input('Parar S ou N :').upper()[0])
    if leave == 'S':
        break
    dados.clear()
totalpessoas = len(pessoas)
for p in pessoas:
    if p[1] > maior:
        maior = p[1]
        pesadas.clear()
        pesadas.append(p[0])
    elif p[1] == maior:
        pesadas.append(p[0])
    if p[1] < menor:
        menor = p[1]
        leves.clear()
        leves.append(p[0])
    elif p[1] == menor:
        leves.append(p[0])
print(f'Total de pessoas : {totalpessoas}')
print(f' o maior peso foi de {maior} kg  das pessoas :{pesadas}')
print(f' o menor peso foi de  {menor} kg das pessoas :   {leves}')



