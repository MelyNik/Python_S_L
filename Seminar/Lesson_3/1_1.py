# Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, определяющую присутствует ли в заданном писке число,
# полученное от пользователя.
# Пример:
# Список 10.
# Число 13.
# [13, 11, 21, 7, 14, 5, 1, 16, 14, 15]
# Да.

# import random
# 
# def Filling_in_the_list(length, mi, ma):
#     array = list(range(length))
#     for i in array:
#         array[i] = random.randint(mi,ma)
#     return array
# 
# def Coincidence(array, number):
#     final = 'No'
#     for l in array:
#         if l == number:
#             final = 'Yes'
#     print(final)
# 
# n = int(input('Введи длину списка: '))
# number = int(input('Введите число: '))
# 
# array = Filling_in_the_list(n, 1, 10)
# print(array)
# 
# print(Coincidence(array, number))

from random import sample

def find_num(number, q):
    q = q if q > 0 else -q # Не знаю, что это значит.
    array = sample(range(1, q * 2), q)
    print(array)
    if number in array:
        return True
    return False

print(find_num(5,3))



