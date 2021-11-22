numero = (
    'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Onze', 'Doze', 'Treze',
    'Quatorze',
    'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    n = int(input('Informe um número'))
    if n >= 0 or n <= 20:
       print(f'O número escolhido por extenso : {numero[n]}')
       break

