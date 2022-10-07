# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности в том же порядке.
# Пример:
# in
# 7
# 
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]
# 
# in
# -1
# 
# out
# Negative value of the number of numbers!
# []
# 
# in
# 10
# 
# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

from random import randint

def Filling_in_the_list(n):
    array = []
    for i in range(n):
        array.append(randint(1,n))
    return array

def Selection_from_the_list(array):
    my_list = []
    for j in range(len(array)):
        if array.count(array[j]) < 2:
            my_list.append(array[j])
    print(my_list)

n = int(input('Введите длину списка: '))

if n < 0:
    print('Negative value of the number of numbers!')
    print('[]')
elif n > -1 and n < 2:
    print('Ошибка!!! Длина списка не подходит.')
else:
    array = Filling_in_the_list(n)
    print(array)
    Selection_from_the_list(array)

