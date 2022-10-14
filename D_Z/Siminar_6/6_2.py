# Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
# Примеры:
# in
# 100
# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100]
# in
# 424
# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100, 105, 120, 126, 140, 147, 160, 168, 180, 189, 
# 200, 210, 220, 231, 240, 252, 260, 273, 280, 294, 300, 315, 320, 336, 340, 357, 360, 
# 378, 380, 399, 400, 420]

def Multiplicity(n):
    if n > 20 or n < -20:
        if n < -20:
            n *= -1
        array = list(range(20,n+1))
        return [array[i] for i in range(len(array)) if not array[i] % 20 or not array[i] % 21]
    print('Eror')


number = int(input('Введите число: '))

print(Multiplicity(number))



# Для себя.


def uniq_list(num):
    return [el for el in range(20, num + 1) if el % 20 == 0 or el % 21 == 0]


print(uniq_list(int(input())))