reta1 = int(input('Informe a reta 1:'))
reta2 = int(input('Informe a 2 reta:'))
reta3 = int(input('Informe a 3 reta:'))


if reta1 > reta2 + reta3 or reta2 > reta1 + reta3 or reta3 > reta2 + reta1:
    print('Nao é um triangulo')
elif reta1 == reta2 and reta2 == reta3 and reta1 == reta3:
    print('Formam um triângulo equilátero')
elif reta1 == reta2 or reta2 == reta3 or reta1== reta3:
    print('Formam um triangulo isóceles')
elif reta1 != reta2 and reta2 != reta3 and reta1 != reta3:
    print('Escaleno')
