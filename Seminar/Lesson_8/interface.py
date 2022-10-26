import excep
import log
import books
import contacts

# Интерфейс только из функций.

def completion_submenu(): # Запускаем функцию подменю.
    # Создаём подменю.
    print('\nХотите выполнить новую операцию?\n \
1 - Да\n \
2 - Нет')
    number_completion_submenu = excep.check_main_menu(3) # К переменой number_completion_submenu присволили функцию excep.check_main_menu(3) - ввод числа и выявление ошибки. 
    # где 3 это значение до которого ошибки ещё не будет.
    if number_completion_submenu == 1:
        return main_menu() # Возвращаем main_menu() если number_completion_submenu == 1.
    else: # Иначе возвращаем заершение работы с программой.
        completion_prog() # Запускаем функцию завершения работы с программой.


def submenu_print_book(): # Запускаем функцию вывода всех контрагентов.
    # Добавили подменю.
    print ('Выберите пункт меню:\n 1 - Вывести перечень всех справочников\n 2 - Главное меню\n 3 - Выход')
    number_submenu = excep.check_main_menu(4) # К переменой number_main_menu присволили функцию excep.check_main_menu(4) - ввод числа и выявление ошибки. 
    # где 4 это значение до которого ошибки ещё не будет.
    if number_submenu == 1: # Если number_submenu == 1, то проваливаемся в if и вызываем функцию books.print_counterparty() для вывода контрагентов.
        books.print_counterparty() # Выводим контрагентов или сообщаем об ошибке.
        completion_submenu() # Запускаем подменю после вывода информации.
    elif number_submenu == 2: # Если number_submenu == 2, то проваливаемся в elif и вызываем функцию main_menu() для выхода в главное меню.
        main_menu() # Запускаем главное меню.
        log.logger("Главное меню", data_description = "Переход") # Запускаем logger
    else:
        completion_prog() # Запускаем функцию завершения работы с программой.


def create_table(): # Запускаем функцию создания справочника (таблицы).
    # Добавили подменю.
    print ('Выберите пункт меню:\n 1 - Создать новый справочник\n 2 - Главное меню\n 3 - Выход')
    number_submenu = excep.check_main_menu(4)# К переменой number_main_menu присволили функцию excep.check_main_menu(4) - ввод числа и выявление ошибки. 
    # где 4 это значение до которого ошибки ещё не будет.
    if number_submenu == 1: # Если number_submenu == 1, то проваливаемся в if и вызываем функцию books.print_counterparty() для создания справочника (таблицы).
        books.create_new_table() # Создаём таблицу или сообщаем об ошибке.
        completion_submenu() # Запускаем подменю после вывода информации.
    elif number_submenu == 2: # Если number_submenu == 2, то проваливаемся в elif и вызываем функцию main_menu() для выхода в главное меню.
        main_menu() # Запускаем главное меню.
        log.ulogger("Главное меню", data_description = "Переход") # Запускаем logger
    else:
        completion_prog() # Запускаем функцию завершения работы с программой.


def open_table(): # Запускаем функцию отрытия справочника (таблицы).
    # Добавили подменю.
    print ('Выберите пункт меню:\n 1 - Открыть справочник\n 2 - Главное меню\n 3 - Выход')
    number_submenu = excep.check_main_menu(4) # К переменой number_main_menu присволили функцию excep.check_main_menu(4) - ввод числа и выявление ошибки. 
    # где 4 это значение до которого ошибки ещё не будет.
    if number_submenu == 1: # Если number_submenu == 1, то проваливаемся в if и вызываем функцию books.open_books() для открытия справочника (таблицы).
        books.open_books() # Открываем справочник (таблицу) или сообщаем об ошибке.
        completion_submenu() # Запускаем подменю после вывода информации.
    elif number_submenu == 2: # Если number_submenu == 2, то проваливаемся в elif и вызываем функцию main_menu() для выхода в главное меню.
        main_menu() # Запускаем главное меню.
        log.logger("Главное меню", data_description = "Переход") # Запускаем logger
    else:
        completion_prog() # Запускаем функцию завершения работы с программой.
        
        
def del_table(): # Запускаем функцию удаления справочника (таблицы).
    # Добавили подменю.
    print ('Выберите пункт меню:\n 1 - Удалить справочник\n 2 - Главное меню\n 3 - Выход')
    number_submenu = excep.check_main_menu(4) # К переменой number_main_menu присволили функцию excep.check_main_menu(4) - ввод числа и выявление ошибки. 
    # где 4 это значение до которого ошибки ещё не будет.
    if number_submenu == 1: # Если number_submenu == 1, то проваливаемся в if и вызываем функцию books.open_books() для открытия справочника (таблицы).
        if excep.check_file('E:\Git\Pyton_S_L\Seminar\Lesson_8\list_table.csv'): # Если из функции excep.check_file('list_table.csv') вернётся True то проваливаемся в IF, иначе в else.
        # В функции excep.check_file('ПУТЬ К ФАЙЛУ'). Т.е. если в файле list_table.csv нет названий справочников (таблиц), то выводим ошибку.
            with open('E:\Git\Pyton_S_L\Seminar\Lesson_8\list_table.csv', 'r', encoding='utf-8') as f_1: # Открываем файл всех справочников (таблицы) в режиме чтения если они есть.
                for line in f_1: # Проходим переменной  line по каждой строке файла f_1.
                    print(line[:-5]) # Выводим каждую строку файла длиной от 0 до -5.
        books.del_book() # Запускаем функцию удаления справочника (таблицы).
        completion_submenu() # Запускаем подменю после вывода информации.
    elif number_submenu == 2: # Если number_submenu == 2, то проваливаемся в elif и вызываем функцию main_menu() для выхода в главное меню.
        main_menu() # Запускаем главное меню.
        log.logger("Главное меню", data_description = "Переход") # Запускаем logger
    else:
        completion_prog() # Запускаем функцию завершения работы с программой.


def add_employee(): # Запускаем функцию добавления сотрудника и выбора справочника (таблицы) куда будем сохранять сотрудника.
    # Добавили подменю.
    print ('Выберите пункт меню:\n 1 - Выберите, в какой справочник внести данные\n 2 - Главное меню\n 3 - Выход')
    number_submenu = excep.check_main_menu(4) # К переменой number_main_menu присволили функцию excep.check_main_menu(4) - ввод числа и выявление ошибки. 
    # где 4 это значение до которого ошибки ещё не будет.
    if number_submenu == 1: # Если number_submenu == 1, то проваливаемся в if и вызываем функцию contacts.create_card и функцию books.open_table_for_work().
        contacts.create_card(books.open_table_for_work())  # Запускаем функцию создания сотрудника зупустив в ней функцию выбора справочника (таблицы) куда сотрудника нужно добавить.
        completion_submenu() # Запускаем подменю после вывода информации.
    elif number_submenu == 2: # Если number_submenu == 2, то проваливаемся в elif и вызываем функцию main_menu() для выхода в главное меню.
        main_menu() # Запускаем главное меню.
        log.logger("Главное меню", data_description = "Переход") # Запускаем logger
    else:
        completion_prog() # Запускаем функцию завершения работы с программой.


def search_employee(): # Запускаем функцию поиска сотрудника.
    # Добавили подменю. 
    print ('Выберите пункт меню:\n 1 - Выбрать справочник\n 2 - Главное меню\n 3 - Выход')
    number_submenu = excep.check_main_menu(4) # К переменой number_main_menu присволили функцию excep.check_main_menu(4) - ввод числа и выявление ошибки. 
    # где 4 это значение до которого ошибки ещё не будет.
    if number_submenu == 1: # Если number_submenu == 1, то проваливаемся в if и вызываем функцию fsearch_contact и функцию books.open_table_for_work().
        contacts.search_contact(books.open_table_for_work()) # Запускаем функцию поиска сотрудника зупустив в ней функцию выбора справочника (таблицы) где будем искать.
        completion_submenu() # Запускаем подменю после вывода информации.
    elif number_submenu == 2: # Если number_submenu == 2, то проваливаемся в elif и вызываем функцию main_menu() для выхода в главное меню.
        main_menu() # Запускаем главное меню.
        log.logger("Главное меню", data_description = "Переход") # Запускаем logger
    else:
        completion_prog() # Запускаем функцию завершения работы с программой.
        
        
def del_card(): # Запускаем функцию удаления сотрудника.
    # Добавили подменю.
    print ('Выберите пункт меню:\n 1 - Выбрать справочник\n 2 - Главное меню\n 3 - Выход')
    number_submenu = excep.check_main_menu(4) # К переменой number_main_menu присволили функцию excep.check_main_menu(4) - ввод числа и выявление ошибки. 
    # где 4 это значение до которого ошибки ещё не будет.
    if number_submenu == 1: # Если number_submenu == 1, то проваливаемся в if и вызываем функцию contacts.del_contact и функцию books.open_table_for_work().
        contacts.del_contact(books.open_table_for_work()) # Запускаем функцию поиска сотрудника и его удаление зупустив в ней функцию выбора справочника (таблицы) где будем искать.
        completion_submenu() # Запускаем подменю после вывода информации.
    elif number_submenu == 2: # Если number_submenu == 2, то проваливаемся в elif и вызываем функцию main_menu() для выхода в главное меню.
        main_menu() # Запускаем главное меню.
        log.logger("Главное меню", data_description = "Переход") # Запускаем logger
    else:
        completion_prog() # Запускаем функцию завершения работы с программой.


def update_card(): # Запускаем фукцию изменения данных сотрудника.
    # Добавили подменю.
    print ('Выберите пункт меню:\n 1 - Выбрать справочник\n 2 - Главное меню\n 3 - Выход')
    number_submenu = excep.check_main_menu(4) # К переменой number_main_menu присволили функцию excep.check_main_menu(4) - ввод числа и выявление ошибки. 
    # где 4 это значение до которого ошибки ещё не будет.
    if number_submenu == 1: # Если number_submenu == 1, то проваливаемся в if и вызываем функцию fsearch_contact и функцию books.open_table_for_work().
        contacts.update_cont(books.open_table_for_work()) # Запускаем функцию поиска сотрудника и его изменение зупустив в ней функцию выбора справочника (таблицы) где будем искать.
        completion_submenu() # Запускаем подменю после вывода информации.
    elif number_submenu == 2: # Если number_submenu == 2, то проваливаемся в elif и вызываем функцию main_menu() для выхода в главное меню.
        main_menu() # Запускаем главное меню.
        log.logger("Главное меню", data_description = "Переход") # Запускаем logger
    else:
        completion_prog() # Запускаем функцию завершения работы с программой.


def completion_prog(): # Функция завершения работы с программой.
    print('\nВыполнение программы завершено. Спасибо!')
    log.logger("по команде пользователя", data_description = "Выход") # Запускаем logger.
    exit() # Функция  exit() завершает работу с программой.

# 1 - Предоставлено меню в Интерфейс.
# Создали список меню попунктно.

def main_menu():
    print('Какое действие Вы хотите выполнить?\n \
1 - Вывести перечень всех справочников\n 2 - Создать новый справочник\n \
3 - Открыть справочник\n 4 - Удалить справочник\n \
5 - Добавить сотрудника\n 6 - Поиск сотрудника\n 7 - Изменить запись сотрудника\n 8 - Удалить запись сотрудника\n 9 - Выход')

    number_main_menu = excep.check_main_menu(10) # К переменой number_main_menu присволили функцию excep.check_main_menu(10) - ввод числа и выявление ошибки. 
    # где 10 это значение до которого ошибки ещё не будет.

    if number_main_menu == 1: 
        return submenu_print_book() # Если число равно 1 возвращаем функцию empl_list(). Почему возвращаем, а не print не могу понять.
    elif number_main_menu == 2:
        return create_table() # Если число равно 2 возвращаем функцию create_table(). Почему возвращаем, а не print не могу понять.
    elif number_main_menu == 3:
        return open_table() # Если число равно 3 возвращаем функцию open_table(). Почему возвращаем, а не print не могу понять.
    elif number_main_menu == 4:
        return del_table() # Если число равно 4 возвращаем функцию del_table(). Почему возвращаем, а не print не могу понять.
    elif number_main_menu == 5:
        return add_employee() # Если число равно 5 возвращаем функцию add_employee(). Почему возвращаем, а не print не могу понять.
    elif number_main_menu == 6:
        return search_employee() # Если число равно 6 возвращаем функцию search_employee(). Почему возвращаем, а не print не могу понять.
    elif number_main_menu == 7:
        return update_card() # Если число равно 7 возвращаем функцию update_card(). Почему возвращаем, а не print не могу понять.
    elif number_main_menu == 8:
        return del_card() # Если число равно 8 возвращаем функцию del_card(). Почему возвращаем, а не print не могу понять.
    else:
        completion_prog() # Запускаем функцию завершения работы с программой.
        
