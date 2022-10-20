# Далее создаём интерфейс в отдельном моуля (файле) view.py

def view_data(data, text): # data - какие-то данные.
    print(f'{text} = {data}') # Выводим какие-то данные.

def get_value():
    return int(input('value = '))