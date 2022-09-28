# Создать список, длина n, значения формируются по формуле 3k+1, 
# где k принимает значения от 1 до n включительно.

import random

n = int(input('Введите число: '))
result = []

for i in range(1,n+1):
    result.append(3*i+1)
print(result)


