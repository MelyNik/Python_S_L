# Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76
# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36

from random import uniform

def Filling_in_the_list(length, mi, ma):
    array = []
    for i in range(length):
        array.append(round(uniform(mi,ma),2))
    return array

def Difference_of_elements(array):
    mi = array[0]
    for i in array:
        if i < mi:
            mi=i
    a = int(mi)
    ma = array[0]
    for i in array:
        if i > ma:
            ma = i
    b = int(ma)
    result = round(((ma - b)-(mi - a)),2)
    print('Min: {}, Max: {}. Difference: {}'.format(mi,ma,result))

n = int(input('Введите длину списка: '))

array = Filling_in_the_list(n, 0, 5)
print(array)

Difference_of_elements(array)
