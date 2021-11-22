while True:
    n = int(input('informe o número da tabuada'))
    if n < 0:
        break
    for i in range(1, 11):
        print(f'{n} * {i} = {n * i}')