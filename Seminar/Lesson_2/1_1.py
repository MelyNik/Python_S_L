# Напишите программу, которая принимает на вход число N 
# и выдаёт последовательность из N членов. 
# Пример:
# >> 5
# >> 1, -3, 9, -27, 81

# 1 Вариант.

number = int(input('Введите число: '))

result = 1

for i in range(number):
    print(result, end=" ")
    result *= -3

# 2 Вариант.

number = int(input('Введите число: '))

for k in range(number):
    print(3**k * (-1)**k, end=" ")

# Или

number = int(input('Введите число: '))

for k in range(number):
    print((-3)**k, end=" ")