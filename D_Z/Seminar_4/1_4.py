# Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (от 0 до 10) многочлена, записать в файл 
# полученный многочлен не менее 3-х раз.
# Пример:
# in
# 9
# 5
# 3
# 
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
# 
# in
# 0
# -1
# 4
# 
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
# 2*x^4 - 3*x^3 + 3*x^2 + 1*x^1 - 2 = 0

from random import choices

def Natural_degree(number):
    if number < 0:
        return 0
    my_text = ''
    my_list = range(0,10)
    with open('my_text.txt', 'a', encoding='utf-8') as my_file:
        for i in range(number, 0, -1):
            k = choices(my_list)
            if k:
                my_text += f"{k}*x^{i} {choices('+-')}"
        my_file.write(f"{my_text}{choices(my_list)} = 0\n")

for j in range(3):
    Natural_degree(int(input()))