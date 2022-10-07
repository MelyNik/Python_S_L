# Найдите корни квадратного уравнения Ax^2 +Bx+C=0,
# с помощью модуля. Запросите значения A,B,C 3 раза.
# Уравнения и корни запишите в файл.

from math import sqrt

def Abc(A,B,C):
    D = B**2 - 4*A*C
    with open('result.txt', 'a', encoding='utf-8') as my_f: # encoding - это режим кодировки в котором мы работаем, 
                                             # т.е. должно быть что то одно например латиница, но в данном случае utf-8.
        my_f.write(f'{A}x^2 + {B}x + {C} = 0\n')
        if D > 0 and A:
            my_f.write(str(( -B + sqrt(D)) / (2 * A)) + '\n')
            my_f.write(str(( -B - sqrt(D)) / (2 * A)) + '\n')
        elif D == 0 and B:
            my_f.write(str( -B / (2 * A)) + '\n')
        else:
            my_f.write('Корней нет\n')

for i in range(3):
    Abc(int(input()), int(input()), int(input()))