nota1 = float(input('Informe sua nota :'))
nota2 = float(input('informe sua outra nota'))

if (nota1 + nota2)/2 < 5:
    print(f'Reprovado com nota {(nota1 + nota2)/2}')

elif (nota1 + nota2) /2 > 5 and (nota1 + nota2)/2 <=6.9:
    print(f'Recuperação {(nota1 + nota2)/2}')

else:
    print(f'Aprovado ! com nota {((nota1 + nota2)/2)}')