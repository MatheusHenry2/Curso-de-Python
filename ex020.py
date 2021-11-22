maior = 0
menor = 9999999

for i in range(0, 5):
    peso = float(input('Informe seu peso:'))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print(f'O maior peso das pessoas é {maior}')
print(f'O menor peso das pessoas é {menor}')


