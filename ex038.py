from random import sample

n = tuple(sample(range(10), 5))
for i in n:
    print(f'{i}', end="  ")
print(f'\n O maior valor : {max(n)} o menor valor : {min(n)}')
