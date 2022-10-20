# model_logger - логирует информацию отдельно о температуре, отдельно о давление и отдельно о скорости ветра.

# Вторым этапом будет логирование по условию, т.е. сразу запись этих данных.

from datetime import datetime as dt # Способ получения даты и времени.

def temperature_logger(data): 
    time = dt.now().strftime('%H:%M') # Таким образм мы получили данные по времени записи температуры %H - часы, %M минуты.
    with open('log.csv', 'a') as file_1:
        file_1.write(f'{time};temperature;{data}\n')


def pressure_logger(data): 
    time = dt.now().strftime('%H:%M') # Таким образм мы получили данные по времени записи температуры %H - часы, %M минуты.
    with open('log.csv', 'a') as file_2:
        file_2.write(f'{time};pressure;{data}\n')



def wind_speed_logger(data): 
    time = dt.now().strftime('%H:%M') # Таким образм мы получили данные по времени записи температуры %H - часы, %M минуты.
    with open('log.csv', 'a') as file_3:
        file_3.write(f'{time};wind_speed;{data}\n')


