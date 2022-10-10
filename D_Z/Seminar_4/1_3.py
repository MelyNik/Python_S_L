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


# Или (для себя)

def Filling_in_the_list1(n):
    array = []
    for i in range(n):
        array.append(randint(1,n))
    return array

def Selection_from_the_list1(array):
    my_list = []
    result = {}.fromkeys(array,0) # Пользуемся методом fromkeys словаря, мы создали словарь в переменную result.
                                  # Где передаём стартовое значение список array ( будет идти ключами).
                                  # Т.е. как я понял в словарь попадают только уникальные ключи и в данном случае в словарь попадут только уникальные числа.
                                  # Даже если в списке array будет 3 одинаковых элемента, например [7, 7, 7] в словарь попадёт только одна цифра 7, остальные не попадут.
                                  # Ключами могут быть int, float, complex, str, кортеж  и frozenset(замороженное множество).
                                  # А второе значение передаём всё нулями.

    for j in array:    # Как я понял в данному случая переменная j пробегая по списку array считает количество каждого элемента
        result[j] += 1 # т.е. в списке [1,3,3,5,6,3,1] подсчитает так 1-2, 3-3, 5-1, 6-1. Получается в словаре result мы создали счётчик.

    for k in result:   # Тут мы пробегам по словарю result и если ключ k==1 то добавляем k в новый список уникальных элементов.
        if result[k] == 1:
            my_list.append(k)
    print(result)

n1 = int(input('Введите длину списка: '))
array = Filling_in_the_list1(n1)
print(array)
Selection_from_the_list1(array)