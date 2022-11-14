from datetime import datetime as dt

def logger(data, data_description = "действие"): 

    time = dt.now().strftime('%d-%m-%Y %H:%M:%S') 
    with open('C:\Новая папка\Lesson\Python_S_L\D_Z\Seminar_10\log.csv', 'a', encoding='utf-8') as file: 
        file.write('{}; {}; {}\n'
                    .format(time, data_description, data)) 