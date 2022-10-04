# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]
# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

from random import sample

def Filling_in_the_list(length,mi, ma):
    my_list = sample(range(mi,ma), length)
    return my_list

def Product_of_list_pairs(array):
    if len(array) % 2 == 0:
        my_list = list(range(len(array)//2)) 
        k = len(array)
        for j in range(len(array) // 2):
            my_list[j] = array[j] * array[k-1]
            k -= 1
        print(my_list)
    else:
        my_list = list(range(len(array)//2 + 1)) 
        k = len(array)
        for j in range(len(array) // 2 + 1):
            if my_list[j] == len(array) // 2:
                my_list[j] = array[len(array) // 2]
            else:
                my_list[j] = array[j] * array[k-1]
                k -= 1
        print(my_list)
        

n = int(input('Введите длину списка: '))

if n == 0:
    print('Ошибка!!! Список не может быть длиной 0')
elif n > 0:
    array = Filling_in_the_list(n,0, 20)
    print(array)
    Product_of_list_pairs(array)
else:
    n = n * (-1)
    array = Filling_in_the_list(n,0, 20)
    print(array)
    Product_of_list_pairs(array)