
number = int(input('Введите число: '))

if (number%5 == 0 and number%10 == 0 or number%15 == 0) and number%30 != 0:
    print('yes')
else:
    print('no')
