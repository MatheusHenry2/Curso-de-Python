palavras = ('teste', 'alou', 'matheus', 'camargo', 'uva', 'elefante', 'abacate')

for i in palavras:
    print(f'\nNa Palavara {i}', end =" ")
    for letra in i:
        if letra.lower() in 'aeiou':
            print(letra, end=" ")
