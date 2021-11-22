frase = str(input('Informe a frase'))
inverso = ""
for palavra in frase.split(" "):
    inverso += palavra[::-1] + ""

print(f'A Palavra que você digitou normal fica {frase} ')
print(f'A frase que você digitou invertida fica: {inverso}')

if frase == inverso:
    print('É um palindromo')
else:
    print('não é um palindromo')
