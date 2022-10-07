# Вычислить число c заданной точностью d
# Пример:
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
# 
# out
# 9.000000
# 
# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001
# 
# out
# 8.988

from decimal import Decimal

def Remains(number,accuracy):
    i = len(accuracy) - 2
    if number % 1:
        print(round(number, i))
    else:
        result = number + float(accuracy) / 10
        print(round(Decimal(result), i))

number = float(input('Enter a real number: '))
accuracy = str(input('Enter the required accuracy "0.0001": '))

Remains(number,accuracy)

# Или ( для себя переписал).

def accuracy_2(num, acc):
    number = Decimal(f"{num}") # Способом f"{num}" как я понял преобразует число в строку, так как Decimal работает только строкой.
    return number.quantize(Decimal(f"{acc}")) # Так как Decimal работает только строкой, acc мы тоже преобразовали.
    # В данному случае мы функцией quantize в строке number добавляем количество знаков после запятой строкой acc.
print(accuracy_2(float(input()), float(input())))

# Или ( для себя переписал).

num = float(input())
accu = input().split('.') # Разбиваем строку на 2 части до . и после .
print(f"{num:.{len(accu)}f}") # Это часть мне не понятна.

