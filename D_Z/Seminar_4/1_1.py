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



