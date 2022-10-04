# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи
# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21
# in
# 5
# out
# 5 -3 2 -1 1 0 1 1 2 3 5


def Negative_fib(n):
    array = [0]
    num_1 = 1
    num_2 = 1
    for i in range(n):
        array.append(num_1)
        array.insert(0, num_1 * (-1)** i)
        num_1, num_2 = num_2, num_1 + num_2
    return array

n = int(input('Введите число: '))

array = Negative_fib(n)
print(array)
