# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27


num = float(input('Введите число: '))
length_num_float = len(str(num))

result_1 = int(num)
length_num_int = len(str(result_1))

conclusion_1 = 0
while result_1 != 0:
    conclusion_1 = conclusion_1 + result_1 % 10
    result_1 //= 10

conclusion_2 = 0
result_2 = str(num)
result_2 = result_2[length_num_int+1:]
result_2 = int(result_2)
while result_2 != 0:
    conclusion_2 = conclusion_2 + result_2 % 10
    result_2 //= 10
final = conclusion_1 + conclusion_2
print(final)

# Или

number = float(input('Введите число: '))
length = len(str(number))
num = number * 10 ** (length-2)

conclusion = 0
while num != 0:
    conclusion = conclusion + num % 10
    num //= 10
print(int(conclusion))