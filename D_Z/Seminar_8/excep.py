import os
from datetime import datetime


def check_main_menu(quan): # Функция на ошибки при вводе данных пользователя на главном меню.
    while True: # while True: try: except ValueError: Мне ещё не знакомы.
        try:
            number_menu = (input()) # К переменной number_menu присваивается число введённое пользвотелем на главном меню.
            while int(number_menu) not in range (1, quan): # Првоерка, если число не в рендже от 1 до quan , то проваливаемся в цикл и просим ввести повторно.
                print ('\nНеверный ввод! Повторите ввод:') 
                number_menu = (input())
            return int(number_menu) # Возвращаем подходящее число к переменной  number_main_menu в интерфейс.
        except ValueError: # Если это вообще не число, то опять же просим ввести число повторно.
            print ('\nНеверный формат! Повторите ввод:')


def check_file(name_file): # Смотрим файл.
    if os.path.exists(name_file): # функцией os.path.exists(name_file) проверяем существует ли файл в переменной name_file, в переменной name_file присвоин путь файла.
        if os.path.getsize(name_file)>0: # Если вес файла больше 0 , то возвращаем True, иначе False.
            return True
        else:
            return False # Возвращаем False так как файл ни чего не весит и скорее всего пустой, а это тоже самое, что его нет (как я понял).
    else:
        return False # Возвращаем False если файла нет по данному пути name_file.


def check_name_table(name_table): # Запускаем функцию проверки имени нового справочника (таблицы) на наличие ошибок ввода
    list_name_table = list(name_table) # В переменную list_name_table добавили список из элементов имени. Т.е. преобразовли текст в список.
    mistake_element = ['/','|','*','?','>','<',':','"','\\'] # Добавили в переменную mistake_element список знаков которые будем считать ошибками.
    for i in list_name_table: # Проходим переменной i по всем элементам списка list_name_table, именно элементам, а не индексам.
        if i in mistake_element or len(name_table)<3: # Если элемет i из списка list_name_table есть в списке mistake_element 
            # или длина строки переменной name_table короче 3, то проваливаемся в if и имя счетается не верным и возвращаем False.
            print ("Недопустимое название")
            return False
    return True # Если предыдущий цикл результата False не дал, то возвращаем True.


def phone(phone): # Запускаем функцию на проверку в номера телефона посторонних знаков, т.е. должны быть только цифры.
    num_for_write = ''.join([i for i in phone if i.isdigit()]) # К переменной num_for_write присваиваем номер телефона, но в строковом виде без пробелов
    # одновременно проверяя что каждый сивол строки это цифра и к переменной num_for_write присваиваем только цифры, пропуская любые другие символы.
    if len(num_for_write) > 3: # Проваливаемся в if если длина номера больше 3.
        return True # Возвращаем  True при условии, что длина номера больше 3.
    else: # Иначе выводим сообщение, что номер телефона не подходит.
        print ("Неверный формат!") # Выводим сообщение.
        return False # И возвращаем False если номер телефона не подходит.

        
def check_data_employee(name): # Запускаем функцию на проверку в фамилии посторонних знаков, т.е. должны быть только буквы.
    if name.isalpha() and len(name)>1: # Функцией .isalpha() проверяем, что в переменной name только буквы и длина строки больше 1, фамилии с одной буквой не будет,
        return True # Возвращаем True если фамилий корректна.
    else:
        return False # Возвращаем False если фамилий не корректна.


def date(date_text): # Запускаем функцию на проверку правильности вводу даты.
    try: # Првоерка на ошибку введённого формата даты.
        bool(datetime.strptime(date_text, '%d.%m.%Y')) # bool возвращает True если утверждение (datetime.strptime(date_text, '%d.%m.%Y')) истина и False если нет.
    except ValueError: # Если формат не верен, то возвращаем False
        print ("Неверный формат!") # Выводим сообщение, что формат не верен.
        return False # Возвращаем False