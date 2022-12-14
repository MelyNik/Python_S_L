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
    if number < 1:
        return 0
    my_text = '' # Переменная куда мы складываем каждую запись многочлена. 
    my_list = range(0,10) # Переменная range всегда будет иметь range от 0 до 10.
    with open('my_text.txt', 'a', encoding='utf-8') as my_file:
        for i in range(number, 0, -1): # Запускаем цикл где range(number, 0, -1) будет идти наоборот т.е. от number до 0, обязательно ставим -1
                                       # что бы range шагал в обратном направлении. 
            k = choices(my_list)       # К переменной k присваиваем случайной число из переменной range, командой choices(my_list)
            if k:                      # Проверка если k > 0,  то строка увеличивается.
                my_text += f"{k}*x^{i} {choices('+-')}" # Далее формируем выражение как в примере, где k это случайный коэффициент, а i это степень
                                                        # подряд по убыванию, а {choices('+-')} случайный знак препинания из ('+-').
        my_file.write(f"{my_text}{choices(my_list)} = 0\n") # Командой my_file.write записали выше заполненный my_text добавив случайное число из my_list, 
                                                            # командой choices(my_list), в конце указали \n, что последующие выражения были на новой строке записаны.

for j in range(3):
    Natural_degree(int(input()))