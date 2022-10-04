# Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# Пример:
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22

from random import sample

def Sum_of_elements_list(length,mi, ma):
    my_list = sample(range(mi,ma), length)
    print(my_list)
    sum = 0
    for i in range(len(my_list)):
        if i % 2 == 0: 
            sum += my_list[i]
    print(sum)

n = int(input('Введите длину списка: '))

if n == 0:
    print('Ошибка!!! Список не может быть длиной 0')
elif n > 0:
    Sum_of_elements_list(n,0, 20)
else:
    n = n * (-1)
    Sum_of_elements_list(n,0, 20)