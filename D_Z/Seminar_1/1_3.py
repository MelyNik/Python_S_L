# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def Finding_the_plane_number(x, y):
    if x > 0 and y > 0:
        return 1
    elif y > 0 and x < 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4 


x = float(input('Введите координат x:'))
y = float(input('Введите координат y:'))

if x == 0 or y == 0:
    print('Error, 0 entered!') 
else:
    print(f'x={x}; y={y} -> {Finding_the_plane_number(x,y)}')

