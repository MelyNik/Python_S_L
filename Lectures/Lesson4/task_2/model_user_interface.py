# model_user_interface - конкретная информация по каждому из данных.

# Третий шаг это интерфейс (view) где консолидируем информацию.

import model_data_provider as prov
import model_logger as log


def temperature_view(sensor): # Если температура то градусы цельсия.
    data = prov.get_temperature(sensor)
    log.temperature_logger(data)
    return data

def pressure_view(sensor): # Если скорость ветра, то например метры в секунду м/с.
    data = prov.get_pressure(sensor)
    log.pressure_logger(data)
    return data


def wind_speed_view(sensor): # Если давление то миллиметр ртутного столба.
    data = prov.get_wind_speed(sensor)
    log.wind_speed_logger(data)
    return data

