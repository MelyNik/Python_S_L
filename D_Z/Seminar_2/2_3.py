# Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# Пример:
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13


n = int(input('Введите длину списка N: '))
array = list(range(n))
for i in array:
    array[i] = int((1 + 1/n) ** n)
print(array)

sum = 0
for i in array:
    sum = sum + array[i]
print(sum)
