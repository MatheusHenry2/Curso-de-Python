times = ('Atletico-mg', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Bragantino', 'Corinthians',
         'internacional', 'Fluminense', 'Cuiabá', 'Athletico-PR')

print('Os 5 primeiros colocados:')
for i in range(0, 5):
    print(times[i], end="  ")

print('\n Os últimos 4 colocados:')
for i in range(9, 5, -1):
    print(times[i], end="  ")

timesS = sorted(times)
print('\n Times em ordem alfabética')
for i in range(0, len(timesS)):
    print(timesS[i], end="  ")

for i in  range (0,len(times)):
    if times[i] == 'Flamengo':
        print(f'\n\nO time flamengo está na posição : {i}')
