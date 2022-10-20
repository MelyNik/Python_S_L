# model_data_provider - модуль который предоставляет данные.

# Модуль получения данных будет первым.

from random import randint

def get_temperature(sensor): # Функция получения температуры.
    return randint(-20, 0) if sensor else randint(0, 20) # Такая письменность подразумевает, что если if sensor то условие до randint(-20, 0), а если else то после randint(0, 20)


def get_pressure(sensor): # Функция получения давления.
    return randint(720, 750) if sensor else randint(750, 770) # Такая письменность подразумевает, что если if sensor то условие до randint(-20, 0), а если else то после randint(0, 20)


def get_wind_speed(sensor): # Функция получения скорости ветра.
    return randint(0, 10) if sensor == 1 else randint(30, 50) # Такая письменность подразумевает, что если if sensor то условие до randint(-20, 0), а если else то после randint(0, 20)


def data_collection(sensor = 1):
    return (get_temperature(sensor), get_pressure(sensor), get_wind_speed(sensor))
