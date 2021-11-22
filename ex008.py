import math
altura = float(input('Informe sua altura :'))
peso = float(input('Informe seu peso:'))

imc = peso/pow(altura, 2)

if imc < 18.5:
    print(f'Abaixo do peso! imc: {imc :.2f}')
elif imc >=18.5 and imc < 25:
    print(f'Peso ideal! imc: {imc :.2f}')
elif imc >=25 and imc < 30:
    print(f'Sobrepeso! imc: {imc :.2f}')
elif imc >= 30 and imc < 40:
    print(f'Obesidade  {imc :.2f}')
else:
    print(f'Obesidade morbida! {imc :.2f}')





