import os
import excep
import log
import interface


def create_new_table(): # Функция создания нового справочника (таблицы).
    name_table = input('Введите имя нового справочника:\n') # Вводим имя нового справочника (таблицы).
    check_name = excep.check_name_table(name_table) # Проверяем имя нового справочника (таблицы) на наличие ошибок ввода, где в скобках функции 
    # excep.check_name_table(name_table) и есть название, нового справочника (таблицы). Т.е. к check_name присваиваем к False или True.
    while check_name is False: # Запускам цикл, если check_name является False, то проваливаемся в цикл для повторного ввода.
        name_table = input('Повторите ввод:\n') # Повторно вводим название таблицы.
        check_name = excep.check_name_table(name_table) # Повторно запускаем проверку наличия ошибок с возвратом False или True.
    else:
        if excep.os.path.isfile(f'E:\Git\Pyton_S_L\Seminar\Lesson_8\{name_table}') is True: # Если путь E:\Git\Pyton_S_L\Seminar\Lesson_8\{name_table}
            # существует то будет True и проваливаемся в if, и сообщаем об ошибке, что такое имя уже есть.
            print("Справочник уже существует!") # Выводим информацию об ошибке.
            log.logger(name_table, data_description = "Ошибка создания справочника, справочник уже существует") # Запускаем logger
        else: 
            # Открываем 2 файла, общий файл всех таблиц и новый файл новой таблицы.
            with open ('E:\Git\Pyton_S_L\Seminar\Lesson_8\list_table.csv','a', encoding='utf-8', newline='') as list_book: # Заходим в файл в режиме дозаписи.
                # зачем тут newline='' - не понял.
                # В файл с талицыми добавляем название новой таблицы.
                list_book.write(f'{name_table}.csv\n') # Записываем и переходим на новую строку.
            with open(f'E:\Git\Pyton_S_L\Seminar\Lesson_8\{name_table}.csv', 'a', encoding='utf-8') as new_table: # Заходим в файл в режиме дозаписи.
                new_table.write('') # Записываем в файл просто пробел, так понимаю, что бы файл имел хоть какой-то вес и не считался в дальнейшем оршибкой.
                print (f'Справочник "{name_table}" успешно создан!') # Сообщаем о успшном создании таблицы.
                log.logger(name_table, data_description = "Создание справочника") # Запускаем logger.


def del_book(): # Запускаем функцию удаления справочника (таблицы).
    if excep.check_file('E:\Git\Pyton_S_L\Seminar\Lesson_8\list_table.csv') is False:# Если из функции excep.check_file('list_table.csv') вернётся False то проваливаемся в IF, иначе в else.
            # В функции excep.check_file('ПУТЬ К ФАЙЛУ')
        print(f'Системная ошибка! Справочники отсутствуют!') # Выводим ошибку.
        log.logger("Справочники отсутсвуют в базе", data_description = "Ошибка удаления справочника") # Запускаем logger.
        interface.completion_submenu() # Запускаем функцию подменю.
    name_table = input('Какой справочник желаете удалить? Введите название:\n') # Вводим имя справочника (таблицы).
    check_name = excep.check_name_table(name_table) # Проверяем имя  справочника (таблицы) на наличие ошибок ввода, где в скобках функции 
    # excep.check_name_table(name_table) и есть название, нового справочника (таблицы). Т.е. к check_name присваиваем к False или True.
    while check_name is False: # Запускам цикл, если check_name является False, то проваливаемся в цикл для повторного ввода.
        name_table = input('Повторите ввод:\n') # Повторно вводим название таблицы.
        check_name = excep.check_name_table(name_table) # Повторно запускаем проверку наличия ошибок с возвратом False или True.
    if excep.os.path.isfile(f'E:\Git\Pyton_S_L\Seminar\Lesson_8\{name_table}.csv'):# Если путь E:\Git\Pyton_S_L\Seminar\Lesson_8\{name_table}
            # существует то будет True и проваливаемся в if.
        print ('Вы уверены?\n 1 - Да\n 2 - Нет') # Повторное уточнение удаления справочника (таблицы).
        del_table = excep.check_main_menu(3) # В переменную number_table возвращаем актуальную цифру введённую пользователем.
        if del_table == 1: # Если del_table == 1, то проваливаемся в if.
            os.remove(f'E:\Git\Pyton_S_L\Seminar\Lesson_8\{name_table}.csv') # Если файл с путём E:\Git\Pyton_S_L\Seminar\Lesson_8\{name_table}.csv существует
            # то функцией os.remove он будет удалён,
            print(f"Справочник {name_table} успешно удален!") # вывели сообщение об успешном удалении.
            log.logger(name_table, data_description = "Удаление справочника") # Запускаем logger.
            with open ('E:\Git\Pyton_S_L\Seminar\Lesson_8\list_table.csv', 'r', encoding='utf-8') as f_1: # Открываем файл list_table.csv список справочников (таблиц) в режиме чтения.
                lines = f_1.readlines() # и создаём список в переменную lines методом f_1.readlines().
            with open ('E:\Git\Pyton_S_L\Seminar\Lesson_8\list_table.csv', 'w', encoding='utf-8') as f_1: # Открываем файл list_table.csv список справочников (таблиц) в режиме записи.
                for line in lines: # Запускаем цикл с условием если в строка line есть в списке lines, то проваливаемся в цикл.
                    if line != name_table+".csv\n": # Если это же строка не равна названию удалённого справочника (таблицы), то снова записываем её в справочник (таблицу).
                        f_1.write(line) # Записываем эту строку,
        elif del_table == 2: # Если del_table == 2, то проваливаемся в elif.
            interface.completion_submenu() # Запускаем функцию подменю.
    else: # Иначе выводим сообщение, что справочника не существует.
        print("Такого справочника не существует!") # Выводим сообщение,
        log.logger(name_table, data_description = "Ошибка удаления справочника, справочник отуствует в базе") # Запускаем logger.


def print_counterparty(): # Функция вывода контрагентов.
        if excep.check_file('E:\Git\Pyton_S_L\Seminar\Lesson_8\list_table.csv'): # Если из функции excep.check_file('list_table.csv') вернётся True то проваливаемся в IF, иначе в else.
            # В функции excep.check_file('ПУТЬ К ФАЙЛУ')
            with open('E:\Git\Pyton_S_L\Seminar\Lesson_8\list_table.csv', 'r', encoding='utf-8') as f_1: # Откываем файл в режиме чтения.
                for line in f_1: # Цикл где line это строка, а f_1.
                    print (f'\nСправочник "{line[:-5]}"\n') # Вывод строки справочника от 0 до -5 (Видимо, что бы конце строки, что то не выводилось).
                    with open(f'E:\Git\Pyton_S_L\Seminar\Lesson_8\{line[:-1]}', 'r', encoding='utf-8') as f_2: # Открываем строку в режиме чтения длиной от 0 до -1 (Видимо, что бы конце строки, что то не выводилось).
                        for line_2 in f_2:
                            print(line_2, end="") # end="" значит, что после print(line_2) вывод следующей команды print, будет на этой же строке и без пробела
                            # но не понятно пока почему.
            log.logger('Перечень контрагентов', data_description = "Запрос") # Запускаем logger
        else: # Если, файла не существует, то выводим ошибку и фиксируем в logger.
            print(f'Системная ошибка! Данные о контрагентах отсутствуют!')
            log.logger("Справочники отсутсвуют в базе", data_description = "Ошибка запроса перечня контрагентов") # Запускаем logger.


def open_books(): # Запускаем функцию отрытия справочника (таблицы).
    if excep.check_file('E:\Git\Pyton_S_L\Seminar\Lesson_8\list_table.csv') is False: # Если из функции excep.check_file('list_table.csv') вернётся False то проваливаемся в IF, иначе в else.
        # В функции excep.check_file('ПУТЬ К ФАЙЛУ'). Т.е. если в файле list_table.csv нет названий справочников (таблиц), то выводим ошибку.
        print(f'Системная ошибка! Справочники отсутствуют!') # Выводим ошибку.
        log.logger("Справочник отуствует в базе", data_description = "Ошибка чтиения справочника") # Запускаем logger.
        interface.completion_submenu() # Запускаем функцию подменю.
    else: # Иначе предлагаем справочник на выбор.
        print ('Какой справочник желаете открыть?') # Выводим сообщение.
        variable_dict = {} # Создаём пустой словарь.
        variable_dict.clear() # Зачем то очистили пустой словарь.
        count = 1 # Создали переменную для нумерации справочников (таблиц).
    with open ('E:\Git\Pyton_S_L\Seminar\Lesson_8\list_table.csv', 'r', encoding='utf-8') as f_1: # Открыли список справочников (таблиц) в режиме чтения.
        for line in f_1: # Проходим переменной line- строка по справочнику (таблице).
            print(f'{count} - Cправочник "{line[:-5]}"') # Выводим номер справочника(таблицы) и название справочника (саму строку) от 0 до -5 длиной.
            variable_dict[count] = line.split() # Создали словарь, и каждый индекс (начиная с цифры 1 (где один это ключ)) добавили каждую строку.
            count += 1 # Увеличиваем переменную на 1.
        # Получается заполнили словарь таблиций где каждый его элемент это отдельная строка c названием отдельной таблице с цифровым ключом.
    number_table = excep.check_main_menu(count) # В переменную number_table возвращаем актуальную цифру введённую пользователем.
    with open(f'E:\Git\Pyton_S_L\Seminar\Lesson_8\{str(*variable_dict[number_table])}','r', encoding='utf-8') as f_2: # Открываем словарь под своим номером в режиме чтения.
        for line in f_2: # Переменной line -  проходим по каждой строке файла f_2.
            print(line, end ='') # Выводим каждую строку причём как я понял на одной строке из за end =''.
    log.logger(f'Открытие справочника {variable_dict[number_table]}', data_description = "Запрос") # Запускаем logger.
    return variable_dict[number_table] # Возвращаем элемент словаря (конкретную таблицу).
  
    
def open_table_for_work(): # Запускаем функцию возврата нужного справочника (таблицы) для дальнейшей работы.
    if excep.check_file('E:\Git\Pyton_S_L\Seminar\Lesson_8\list_table.csv') is False:# Если из функции excep.check_file('list_table.csv') вернётся False то проваливаемся в IF, иначе в else.
        # В функции excep.check_file('ПУТЬ К ФАЙЛУ'). Т.е. если в файле list_table.csv нет названий справочников (таблиц), то выводим ошибку.  
        print(f'Системная ошибка! Справочники отсутствуют!') # Выводим ошибку.
        log.logger("Справочник отуствует в базе", data_description = "Ошибка чтения справочника") # Запускаем logger.
        interface.completion_submenu() # Запускаем функцию подменю.
    print ('Какой справочник хотите использовать?') # Выводим сообщение.
    with open('E:\Git\Pyton_S_L\Seminar\Lesson_8\list_table.csv', 'r', encoding='utf-8') as f_1: # Открыли список справочников (таблиц) в режиме чтения.
        variable_dict = {} # Создаём пустой словарь.
        variable_dict.clear() # Зачем то очистили пустой словарь.
        count = 1 # Создали переменную для нумерации справочников (таблиц).
        for line in f_1: # Проходим переменной line- строка по справочнику (таблице).
            print(f'{count} - Cправочник {line[:-5]}\n', end='') # Выводим номер справочника(таблицы) и название справочника (саму строку) от 0 до -5 длиной.
            variable_dict[count] = line.split() # Создали словарь, и каждый индекс (начиная с цифры 1 (где один это ключ)) добавили каждую строку.
            count += 1 # Увеличиваем переменную на 1.
    number_table = excep.check_main_menu(count) # В переменную number_table возвращаем актуальную цифру введённую пользователем.
    return variable_dict[number_table] # Возвращаем элемент словаря (конкретную таблицу).