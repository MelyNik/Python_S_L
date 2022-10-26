import excep
import interface
import log


def dictionary_data(key): # Запускаем функцию созданию карточки сотрудника, где key будет ключом в словаре.
    card_data = {1: "фамилию", 2: "имя", 3: "отчество", 4: "номер телефона",
                  5: "дату вступления в должность в формате ДД.ММ.ГГГГ", 6: "должность"} # Создали словарь с ключами и названиеми.
    return card_data.get(key) # Возвращаем словарь и берём данные  key который совпадают с ключом из словаря card_data.
    
    
def enter_data(): # Запускаем функцию ввода данных сотрудника.
    card_list = [] # Создаём пустой список который в дальнейшем будет хранить данные сотрудника.
    card_list.clear() # Зачем то очищаем пустой список.
    count = 0 # Создаём пустую переменную.
    # Следующим циклом for вводим все данные пользователя по порядку.
    for i in range (1,6): # Запустили список длинной от 1 до 6 потому, что вего 6 пунктов в словаре card_data функции 
        data = input(f'Введите {dictionary_data(i)}:\n') # Получается в переменную data присваивается фамилия которая подтягивается 
        # вводом пользовтеля через функцию card_data и словарь card_data.
        if i == 4: # Если число 4, то проверяем на ошибки номер телефона.
            while excep.phone(data) is False: # Проверяем на ошибки номер телефона. Если возвращается False значит номер не верный и проваливаемся в цикл.
                data = input (f'Введите {dictionary_data(i)}:\n') # Повторно к переменной data присваиваем номер телефона.
            data = ''.join([i for i in data if i.isdigit()]) # Если номер телефона подходит то минуем цикл и преобразуем переменную data в строку взяв только цифры.
        elif i == 5: # Если число 5, то проверяем на ошибки фиксацию даты.
            while excep.date(data) is False: # Проверяем на ошибки ввод даты. Если возвращается False значит дата не верна и проваливаемся в цикл.
                data = input(f'Введите {dictionary_data(i)}:\n') # Повторно к переменной data присваиваем дату.
        else: # else задействована если i = 1, 2, 3 или 6 из за того, что в данном else работа происходит с текстом, а в других i - 4 и 5 с числами и датами.
            while excep.check_data_employee(data) is False: # А дальше проверка на ошибки введённой фамилии, 
                # т.е. вернётся  False или True при условии, что фамилия состоит только из букв. Если вернётся False то фамилия не корректна и проваливаемся в цикл.
                print('Неверный ввод! Повторите ввод!') # Вывод сообщения об ошибке.
                data = input (f'Введите {dictionary_data(i)}:\n') # Повторно к переменной data присваиваем фамилию.
            data = data.lower() # Переменной data присвоили те же данные, но переведя в нижний регистр, но это не нужно, так как следующая функция .capitalize() 
            # Переводит всю строку в нижний регистр, а первую букву в верхний регистр.
            data = data.capitalize() # Переводит первую букву строки в верхний регистр.
        card_list.append(data) # Добавляем в список card_list полученные данные по порядку.
    print('Выберите должность:\n') # Когда i становится 6 выводим сообщение.
    with open('E:\Git\Pyton_S_L\Seminar\Lesson_8\Post.csv', 'r', encoding='utf-8') as f_1: # Открываем для чтения файл с должностями для выбора.
        for line in f_1: # Как обычно проходим по каждой строке этого файла.
            print(f" {line}", end = '') # Выводим на экран каждую строку. Т.е. каждую должность.
            count+=1 # Увеличиваем переменную.
        print() # Пропускаем строку каждый раз привыводе.
    number_post = excep.check_main_menu(count+1) # К переменной number_post присваиваем номер жедаемой должности и выпоняем проверку на правильность ввода.
    with open('E:\Git\Pyton_S_L\Seminar\Lesson_8\Post.csv', 'r', encoding='utf-8') as f_1: # Снова открываем для чтения файл с должностями для выбора.
        for i, line in enumerate(f_1, start=1): # Функцией enumerate(f_1) мы возвращаем кортежи, где i будет нумерацией начиная с 0, а line строка в файле f_1.
            # start=1 обозначили, что нумерация i начнётся не с 0, а с 1.
            if i == number_post: # Проверка введённый номер пользователя равен ли счётчику i и если да проваливаемся в if.
                card_list.append(line.split('-')[1][1:]) # Дабавляем подходящую строку в список тем самым завершая его.
                # В таблице должность указано всё с ключами например (1 - дизайнер), но нам нужно, что бы в карточку сотрудника попадало только  (дизайнер)
                # без (1 -), для этого мы сразу создали ещё один список в списке через split('-'), гдн разделителем будет '-', и у нас получился список
                # [1, дизайнер], и таким образом мы сообщили [1][1:], что из этого списка берём только элемент с индексом [1], и далее [1:].
    return card_list # Возвращаем список из данных одного сотрудника.
    

def create_card(table): # Запускаем функцию записи нового сотрудника в конкретный справочник  (таблицу) table.
    data = enter_data() # к переменной data присваиваем функцию ввода данных сотрудника enter_data().
    with open(f'E:\Git\Pyton_S_L\Seminar\Lesson_8\{str(*table)}', 'r', encoding='utf-8', newline='\n') as f_1: # Открываем справочник (таблицу) table в режме чтения методом *table. Зачем newline='\n' не могу понять.
        rd = f_1.readlines() # В переменную rd создаём список из строк файла f_1
        i = 0 # Создаём перменную i
        if rd: # Если rd не пустой то проваливаемся в if.
            temp_number = (rd[-1].split(',')) # К переменной temp_number присвоили словарь с последним элементов, но точно как не могу понять из за словаря.
            # Как я понял переменной temp_number мы вычисляем ключ созданного нового сотрудника, но не могу поянять как.
            i = temp_number[0] # К переменной i присвоили элемент списка temp_number с индексом 0.
        data.insert(0, int(i)+1) # В список data (данные сотрудника) добавили в нулевой индекс ключ командой data.insert(0, int(i)+1), где int(i)+1 будет номер ключа.
    with open(f'E:\Git\Pyton_S_L\Seminar\Lesson_8\{str(*table)}', 'a', encoding='utf-8') as f_1: # Открываем файл *table (справочник(таблица)) в режиме дозаписи, что бы записать созданного сотрудника.
        card = [str(a) for a in data] # В переменную card записываем строку из данных сотрудника одновременно преобразовав через цикл из списка в строку.
        f_1.write(f'{",".join(card)}') # Записываем эти данные в справочник(таблицу).
        print (f'Данные о контрагенте сохранены в справочнике!') # Выводим сообщение об успешном сохранении.
        log.logger(f'{data[1]} {data[2]} {data[3]}', data_description = "Создан новый контрагент") # Запускаем logger.
    



def search_contact(table): # Запускаем функцию поиска сотрудника и выбора справочника (таблицы) где будем искать.
    with open(f'E:\Git\Pyton_S_L\Seminar\Lesson_8\{str(*table)}', 'r', encoding='utf-8') as f_1: # Открываем нужный справочник (таблицу) в режими чтения.
        data = f_1.readlines() # К переменной data присваиваем список из строк открытого справочника (таблицы).
    
    def search(data): # Запускаем функцию поиска сотрудника.
        counter = 1 # Создали счётчик.
        name = input('Введите имя, фамилию, или номер телефона:\n') # К переменной name запросили ввод любого из данных сотрудника.
        name = name.lower() # Переменной name присвоили те же данные, но переведя в нижний регистр, но это не нужно, так как следующая функция .capitalize() 
        name = name.capitalize() # Переводит первую букву строки в верхний регистр.
        global count_find_cont # Глобализируем переменную (счётчик) count_find_cont, что бы можно было исполььзовать её везде именно в этом контексте.
        count_find_cont = 0 # Присвоили к этой перменной 0.
        for i in data: # Запускаем цикл проходящий элементами по списку где i элемент, а файл data в ввиде списка
            if name in i: # Если переменная  name есть в элементе i, то проваливаемся в if, 
                counter = 0 # Обнулили счётчик.
                count_find_cont+=1 # Если было совпадение, то в глобальную переменную увеличиваем +1.
                print(f"\033[32m {i} \033[39m") # Выводим i (все данные о найденном сотруднике) стилизированным образом.
                name = i # К переменной name присваиваем всю строку с данными найденного пользователя.
                log.logger(f'{name}, справочник {table}', data_description = "Найден контакт по запросу") # Запускаем logger.
        if counter: # Если пользователь был не найден, то переменная counter остаётся положительной тем самым истеной True и проваливаемся в if.
            print('Совпадений не найдено') # Вывели сообщение, что совпадений не найдено.
            name = '' # К переменной name присваиваем пустое так скажем место.
            log.logger(name, data_description = "Поиск контрагента, совпадений не найдено") # Запускаем logger.
        return name # Возвращаем все данные найденного  или не найденного сотрудника.
    name = search(data) # К переменной name присваиваем функцию поиска сотрудника.
    return name # # Возвращаем все данные найденного  или не найденного сотрудника.


def del_contact(table): # Запускаем функцию удаления сотрудника.
    print ('Данные какого контрагента вы хотите удалить?') # Выводим сообщение.
    card_del = search_contact(table) # К переменной присваиваем функцию поиска сотрудника и выбора справочника (таблици) где будем искать.
    if card_del == '': # Если в переменной search будет пустое значение, значит сотрудник не найден и проваливаемся в if.
        interface.completion_submenu() # Запускаем функцию подменю.
    if count_find_cont !=1: # Если глобальная переменная больше чем 1 , то значит нашли несколько пользователей и просим уточнить запрос.
        print (f'Найдено {count_find_cont} контрагентов! Уточните запрос!') # Вывели сообщение если выводися больше 1 сотрудника.
        log.logger(card_del, data_description = "Удаление не выполнено, неполный запрос") # Запускаем logger.
        interface.completion_submenu() # Запускаем функцию подменю.
    else: # Добавили подменю подтверждения операции. 
        print ('Вы уверены?\n 1 - Да\n 2 - Нет')
        number_submenu = excep.check_main_menu(3) # К переменой number_main_menu присволили функцию excep.check_main_menu(4) - ввод числа и выявление ошибки. 
    # где 4 это значение до которого ошибки ещё не будет.
        if number_submenu == 1: # Если number_submenu == 1 открываем справочник (таблицу) сотрудников. 
            with open(f'E:\Git\Pyton_S_L\Seminar\Lesson_8\{str(*table)}', 'r', encoding='utf-8') as f_1: # Открываем справочник (таблицу) сотрудников в режиме чтения.
                data = f_1.readlines() # К переменной data присваиваем список из строк открытого справочника (таблицы).
            with open(f'E:\Git\Pyton_S_L\Seminar\Lesson_8\{str(*table)}', 'w', encoding='utf-8') as f_1: # Открываем справочник (таблицу) сотрудников в режиме записи.
                for line in data: # Запускаем цикл переменной line проходя по списку  data.
                    if card_del != line: # Если данные для удаления card_del не равны строки (элементу) line, то снова записываем в файл.
                        f_1.write(line) # Записываем в файл.
                print('Удаление завершено!')
            log.logger(card_del, data_description = "Удаление контрагента") # Запускаем logger.
        else:
            interface.completion_submenu() # Запускаем функцию подменю.



def update_cont(table): # Запускаем функцию поиска сотрудника и его изменение зупустив в ней функцию выбора справочника (таблицы) где будем искать.
    search = search_contact(table) # К переменной присваиваем функцию поиска сотрудника и выбора справочника (таблици) где будем искать.
    if search == '': # Если в переменной search будет пустое значение, значит сотрудник не найден и проваливаемся в if.
        interface.completion_submenu() # Запускаем функцию подменю.
    if count_find_cont !=1:  # Если глобальная переменная больше чем 1 , то значит нашли несколько пользователей и просим уточнить запрос.
        # Добавили подменю. 
        print (f'Найдено {count_find_cont} контрагентов! Изменение бужет выполнено для последнего из списка. Продолжить?\n \
1 - Продолжить\n 2 - Уточнить запрос\n 3 - Выход')
        number_submenu = excep.check_main_menu(4) # К переменой number_main_menu присволили функцию excep.check_main_menu(4) - ввод числа и выявление ошибки. 
    # где 4 это значение до которого ошибки ещё не будет.
        if number_submenu == 1: # Если number_submenu == 2 то вызываем функцию return_change_card для изменения данных сотрудника. 
            return_change_card(search, table) # Запускаем функцию для изменения данных сотрудника.
        elif number_submenu == 2: # Если number_submenu == 2 то вызываем саму же функцию update_cont. 
            update_cont(table) # Вызываем функцию.
        else:
            interface.completion_submenu() # Запускаем функцию подменю.
    else:
        return_change_card(search, table) # Запускаем функцию return_change_card для изменения данных сотрудника. 


def return_change_card(employee, table): # Запуск функции возвращения изменённого контакта.
    employee_id = input('Для подтверждения - введите id записи: ') # К переменной employee_id присваиваем введённое пользователем число (id) которое ранее вывели на экран.
    while not employee_id in employee.split(','): # Если employee_id отсутствует в списке employee.split(',') данных пользовтеля сообщаем об ошибке.
        print (f'Неверный id записи!') # Cообщаем об ошибке
        employee_id = input('Для подтверждения - введите id записи: ') # Повторно просим ввести id сотрудника.
    else: # Если id указан верно проваливаемся в else.
        # Добавили подменю.
        print ('Какие данные желаете изменить?\n 1 - Фамилию\n 2 - Имя\n 3 - Отчество\n \
4 - Номер телефона\n 5 - Дату вступления в должность\n 6 - Должность\n 7 - Выход')
        choice_change = excep.check_main_menu(8) # К переменой number_main_menu присволили функцию excep.check_main_menu(4) - ввод числа и выявление ошибки. 
    # где 4 это значение до которого ошибки ещё не будет.
        if choice_change == 7: # Если choice_change == 7 то завершаем работу с программой. 
            interface.completion_submenu() # Запускаем функцию подменю.
        data_change = input(f"Введите {dictionary_data(choice_change)}:\n") # К переменной data_change присваивается запись из словаря по ключу и просим ввести новые данные.
        if choice_change in [1,2,3,6]: # Если choice_change есть в списке [1,2,3,6] проваливаемся в if.
            while excep.check_data_employee(data_change) is False: # Проверяем переменную data_change на правильность ввода текстовых данных если введены не верно вернётся False.
                # Если вернулось False проваливаемся в цикл 
                print('Невернй ввод! Повторите ввод!') # Выводим сообщение об ошибке.
                data_change = input (f'Введите {dictionary_data(choice_change)}:\n') # Просим повторно ввести данные.
                data_change = data_change.lower() # Переменной data присвоили те же данные, но переведя в нижний регистр, но это не нужно, так как следующая функция .capitalize() 
            # Переводит всю строку в нижний регистр, а первую букву в верхний регистр.
                data_change = data_change.capitalize() # Переводит первую букву строки в верхний регистр.
        elif choice_change == 4: # Если choice_change == 4 то проваливаемся в elif. 
            while excep.phone(data_change) is False: # Проверяем на ошибки номер телефона. Если возвращается False значит номер не верный и проваливаемся в цикл.
                choice_change = excep.phone(input (f'Введите {dictionary_data(choice_change)}:\n')) # Просим ввести повторно.
        elif choice_change == 5: # Если choice_change == 5 то проваливаемся в elif. 
            while excep.check_date is False: # Проверяем на ошибки ввод даты. Если возвращается False значит дата не верна и проваливаемся в цикл.
                choice_change = excep.check_data_employee(input (f'Введите {dictionary_data(choice_change)}:\n')) # Просим ввести повторно.
        ident = '' # Создали пустую строку.
        with open(f'E:\Git\Pyton_S_L\Seminar\Lesson_8\{str(*table)}', 'r', encoding='utf-8') as f_1: # Открыли в режиме чтения справочник (таблицу) сотрудников.
            data = f_1.readlines() # В переменную data присвоили список из элементов строк этого файла f_1.
        with open(f'E:\Git\Pyton_S_L\Seminar\Lesson_8\{str(*table)}', 'w', encoding='utf-8') as f_2: # Открыли в режиме записи справочник (таблицу) сотрудников.
            for i in data: # Запускаем цикл переменной i проходя по списку  data.
                temp = i.split(',') #  В список temp добаляем первый элемент списка data. Т.е. в список temp добавили строку данных конкретного сотрудника.
                ident = temp[0] # В переменную ident добавили элемент списка temp с индексом 0 ( это будет id).
                if ident == employee_id: # Если вводимый ранее id(employee_id) совпадает с ident, то проваливаемся в if.
                    temp[choice_change] = data_change # В элемент списка с индексом choice_change добавляем новую информацию data_change.
                    line = [str(a) for a in temp] # В список line комплектуем строками все элементы списка temp включая уже изменённый.
                    f_2.write(",".join(line)) # Преобразуем список line строку отделяя элементы запятыми и записываем в файл f_2.
                    print (f'Данные о контрагенте сохранены в справочнике!') # Выводим сообщение, что данные сохранены.
                else: # Иначе в этом элементе списка data мы не находим данные.
                    line = [str(a) for a in temp] # В список line комплектуем строками все элементы списка.
                    f_2.write(",".join(line)) # Преобразуем список line строку отделяя элементы запятыми и записываем в файл f_2.
        log.logger(f"{employee[:-1]}, измененили - {dictionary_data(choice_change)}", data_description = "Изменение данных пользователя") # Запускаем logger.