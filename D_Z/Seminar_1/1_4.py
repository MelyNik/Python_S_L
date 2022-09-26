# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).


## Для себя:
## import random
## 
## def Decision(number):
##     if number < 5 and number > 0:
##         if number == 1:
##             a1 = round(random.uniform(1,10),3)
##             a2 = round(random.uniform(1,10),3)
##             b1 = round(random.uniform(1,10),3)
##             b2 = round(random.uniform(1,10),3)
##             return round(((((a1-b1)**2)+((a2-b2)**2))**(0.5)),2)
##         elif number == 2:
##             a1 = round(random.uniform(-10,0),3)
##             a2 = round(random.uniform(1,10),3)
##             b1 = round(random.uniform(-10,0),3)
##             b2 = round(random.uniform(1,10),3)
##             return round(((((a1-b1)**2)+((a2-b2)**2))**(0.5)),2)
##         elif number == 3:
##             a1 = round(random.uniform(-10,0),3)
##             a2 = round(random.uniform(-10,0),3)
##             b1 = round(random.uniform(-10,0),3)
##             b2 = round(random.uniform(-10,0),3)
##             return round(((((a1-b1)**2)+((a2-b2)**2))**(0.5)),2)
##         else:
##             a1 = round(random.uniform(1,10),3)
##             a2 = round(random.uniform(-10,0),3)
##             b1 = round(random.uniform(1,10),3)
##             b2 = round(random.uniform(-10,0),3)
##             return round(((((a1-b1)**2)+((a2-b2)**2))**(0.5)),2)
##     else:
##         return
## 
## number = int(input('Введите номер четверти: '))
## print(Decision(number))
## 
## 

# Решение.

from unittest import result


def Possible_coordinates(number):
    if number == 1:
        return 'x > 0, y > 0'
    elif number == 2:
        return 'x < 0, y > 0'
    elif number == 3:
        return 'x < 0, y < 0'
    elif number == 4:
        return 'x > 0, y < 0'
    else: 
        return 'The quarter is entered incorrectly!'

number = int(input('Введите номер четверти плоскости: '))
print(Possible_coordinates(number))

