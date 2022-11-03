from datetime import datetime as dt

# Создали логирование.

def logger(data, data_description = "действие"): 

    time = dt.now().strftime('%d-%m-%Y %H:%M:%S') # К переменной time добавили дату и время в формате '%d-%m-%Y %H:%M:%S'
    with open('Pyton_S_L\D_Z\Seminar_9\log.csv', 'a', encoding='utf-8') as file: # Открыли файл logger.csv для дозаписи, где logger.csv это называние файла и путь к нему.
        file.write('{}; {}; {}\n'
                    .format(time, data_description, data)) 