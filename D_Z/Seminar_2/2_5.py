# Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# Пример:
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

import random

array = list(range(10))
print(array)

for i in array:
    k = random.randint(0, 9)
    temp = array[i]
    array[i] = array[k]
    array[k] = temp
print(array)


# Или

array1 = list(range(10))
print(array1)
for i in range(len(array1)):
    n_1 = random.randrange(len(array1))
    n_2 = random.randrange(len(array1))
    array1[n_1], array1[n_2] = array1[n_2], array1[n_1]
print(array1)

