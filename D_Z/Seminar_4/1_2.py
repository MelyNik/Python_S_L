# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Простые делители числа
# Пример:
# in
# 54
# 
# out
# [2, 3, 3, 3]
# 
# in
# 9990
# 
# out
# [2, 3, 3, 3, 5, 37]
# 
# in
# 650
# 
# out
# [2, 5, 5, 13]

def List_of_prime_factors_of_a_number(number):
    array = []
    i = 2
    while number != 1:
        if not number % i:
            number = number // i
            array.append(i)
        else:
            i+=1
    return array

number = int(input('Введите число: '))


if number > 1:
    array = List_of_prime_factors_of_a_number(number)
    print(array)
else:
    print('Простых множителей у числа',number,'нет.')






