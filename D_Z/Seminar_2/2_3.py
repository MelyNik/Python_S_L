# Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# Пример:
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13


n = int(input('Введите длину списка N: '))
array = list(range(n))
sum = 0

for i in array:
    array[i] = int((1 + 1/n) ** n)
    sum += array[i]

print(array)
print(sum)

# Или

n = int(input('Введите длину списка N: '))
array1 = []
sum1 = 0

for i in range(1,n+1):
    result = round((1 + 1/i) ** i)
    array1.append(result)
    sum1 += result

print(array1)
print(sum1)
