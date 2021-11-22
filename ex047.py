expressao = str(input('Informe a expressao'))
left = 0
right = 0
for i in expressao:
    if '(' in i:
        left = left + 1
    if ')' in i:
        right = right + 1
if right == left:
    print('A expressão é válida!')
else:
    print('A expressão não é válida')