# Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, 
# заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях(не индексах).
# Пример:
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15

number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))

n = int(input('Введите длину списка N: '))
list = []

for i in range(-n,n+1):
    list.append(i)
print(list)

if number_1 < ((n * 2) + 1) and number_1 > -((n * 2) + 1):
    if number_2 < ((n * 2) + 1) and number_2 > -((n * 2) + 1):
        composition = list[number_1-1] * list[number_2-1]
        print(composition)
    else:
        print('Ошибка!!! Один из элементов не в диапазоне списка!')
else:
    print('Ошибка!!! Один из элементов не в диапазоне списка!')

