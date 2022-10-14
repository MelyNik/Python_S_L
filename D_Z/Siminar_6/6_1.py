# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента. Use comprehension.
# Пример:
# in
# 9
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]
# in
# 10
# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

from random import sample

def Result(size):
    array = sample(range(size*2), size)
    print(array)
    return [array[i] for i in range(1,len(array)) if array[i] > array[i - 1]]

size = int(input('Введите длину списка: '))
print(Result(size))



# Для разбора

from random import randint


def more_then(num):
    original_list = [randint(0, 1000) for _ in range(num)]
    print(original_list)
    return [num for i, num in enumerate(original_list[1:]) if num > original_list[i]]


print(more_then(int(input())))


