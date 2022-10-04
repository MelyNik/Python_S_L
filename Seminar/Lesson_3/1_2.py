# Задайте список, состоящий из произвольных слов, количество задаёт пользователь.
# Напишите программу, которая определит индекс второго вхождения строки
# в списке либо сообщит, что её нет.

# Мой вариант:

# def Dilling_in_the_list_manually_with_text(length):
#     array = list(range(n))
#     for i in range(n):
#         print('Введите', i+1, 'элемент ')
#         array[i] = input()
#     return array
#
# def Search_for_a_list_item_by_index(coincidence):
#     k = 0
#     j = 0
#     for l in range(len(array)):
#         if array[l] == line:
#             k+=1
#         if k == coincidence:
#             j = l
#     if k > coincidence-1:
#         return j
#     return '-1'
#
# n = int(input('Введи длину списка: '))
#
# array = Dilling_in_the_list_manually_with_text(n)
# print(array)
#
# line = input('Введите строку: ')
#
# print(Search_for_a_list_item_by_index(2))

# Или

from random import choices


def Name(length, text):
    array = []
    for i in range(length):
        t = choices(text, k=3)  # k - клина новой строковой переменной,
        # т.е. в функции рэндома choices, мы берём из строковой переменной  text 3 случайные элементы k.
        # и ниже в новый список в конец добавляем новую переменную t заполненную случайными буквами из переменной t.
        array.append(''.join(t))
    return array


# Таким образом мы уточнили, что array это список.
def Find(text, array: list):
    # Таким образом мы поняли, что text встречается в списке array больше 1 раза если true.
    if array.count(text) > 1:
        # Данной функцией мы нашли индекс первого совпадения переменной text в списке array.
        o = array.index(text)
        # Таким же методом добавив к переменной о + 1 мы нашли индекс второго совпадения.
        print(array.index(text, o + 1))
    else:
        print('-1')


array = Name(20, 'zxy')
print(array)
Find('zxy', array)
