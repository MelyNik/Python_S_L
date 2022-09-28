# Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# Пример:
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

import random

array = list(range(10))

for i in array:
    array[i] = i
print(array)

for i in array:
    k = random.randint(0, 9)
    temp = array[i]
    array[i] = array[k]
    array[k] = temp
print(array)
