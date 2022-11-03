
import telebot
import log
from random import choice

# К Переменной tokken присваиваиваем наш уникальный токкен.
tokken = '5704215037:AAFtYNTzAF4Y0_D4XPlOH8NWU1VlEbNojwQ' # Отдельным модулем не получилось, все время писал "No module named 'TOK'"
tok = telebot.TeleBot(tokken) # К переменной tok фиксируем наш таккен в боте.
buttons_1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] 
buttons_2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] 

def win_combinations(data): # Функция с выигранными комбинациями.
    win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)) # Переменной win создали кортежи индексов для удобно выгрузки в из buttons_1.
    for i in win: # Создали цикл прохождения по переменной win.
        if data[i[0]] == data[i[1]] == data[i[2]] : # Если уже изменённые элементы в списке buttons_1 будут равны друг другу по индексам из win то проваливаемся в if.
            return True # Возвращаем True если выигрыш.
    return False # Возвращаем False если проигрыш.


@tok.message_handler(commands = ['start']) # Данной командой сообщаем боту, что нужен ответ после надписи пользователем start.
def start_message(message): # Создаём функцию ответа бота пользователю.
    log.logger('start','Запуск бота командой start') # Запускаем логгер.
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 3) # Данный способ создания клавиатуры в телеграмм, где row_width это ширина поля.
    button_1 = telebot.types.KeyboardButton(f'{buttons_1[0]}') # Создаём кнопку.
    button_2 = telebot.types.KeyboardButton(f'{buttons_1[1]}') # Создаём кнопку.
    button_3 = telebot.types.KeyboardButton(f'{buttons_1[2]}') # Создаём кнопку.
    button_4 = telebot.types.KeyboardButton(f'{buttons_1[3]}') # Создаём кнопку.
    button_5 = telebot.types.KeyboardButton(f'{buttons_1[4]}') # Создаём кнопку.
    button_6 = telebot.types.KeyboardButton(f'{buttons_1[5]}') # Создаём кнопку.
    button_7 = telebot.types.KeyboardButton(f'{buttons_1[6]}') # Создаём кнопку.
    button_8 = telebot.types.KeyboardButton(f'{buttons_1[7]}') # Создаём кнопку.
    button_9 = telebot.types.KeyboardButton(f'{buttons_1[8]}') # Создаём кнопку.
    keyboard.add(button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9) # Добавляем в клавиатуру keyboard все кнопки button.
    send_message = f'Привет, {message.from_user.first_name}! Добро пожаловать в игру крестики-нолики!' # К переменной send_message присваиваем приветствие пользователя
                                                                                                       # где from_user.first_name будет распозновать его имя в телеграмм.
    tok.send_message(message.chat.id, send_message, reply_markup = keyboard) # Это уже сам вывод сообщения от бота к пользователю, где send_message само сообщение, а 
                                                                      # reply = keyboard вывести клавиатуру после сообщения.
    log.logger('Привет, {message.from_user.first_name}! Добро пожаловать в игру крестики-нолики!', 'ответ бота') # Запускаем логгер.

@tok.message_handler(content_types = ['text']) # Данной командой сообщаем боту, что нужен ответ после надписи пользователем start.
def mes(message):
    counter_1 = 0
    counter_2 = 0
    draw = 0 # Созадли переменную для фиксации если уже была сыграна партия в ничью.
    get_msgmessage_bot = message.text.split() # В переменную добавляем полученное сообщение от пользователя.
    try:
        button = int(get_msgmessage_bot[0]) # проверка на числовое значение в кнопке
    except:
        button = 0 # Если пользовтель ввёл не подходящее значение, то к button присваиваем 0.
    if button > 0 and button < 10: # проверка на вход числа в числовой промежуток клавиатуры.
        if str(buttons_1[button - 1]) in buttons_2:
            for i in range(len(buttons_2)):
                if str(buttons_1[button - 1]) == buttons_2[i]:
                    counter_1 = i
                    counter_2 = 1
        if counter_2:
            buttons_2.pop(counter_1)
        log.logger(button, 'ходит пользователь') # Запускаем логгер.
        buttons_1[button - 1] = 'X' # В списке меняем элементы на нужные нам значения, например 'X'.
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 3) # Данный способ создания клавиатуры в телеграмм, где row_width это ширина поля.
        button_1 = telebot.types.KeyboardButton(f'{buttons_1[0]}')  # Создаём кнопку.
        button_2 = telebot.types.KeyboardButton(f'{buttons_1[1]}')  # Создаём кнопку.
        button_3 = telebot.types.KeyboardButton(f'{buttons_1[2]}')  # Создаём кнопку.
        button_4 = telebot.types.KeyboardButton(f'{buttons_1[3]}')  # Создаём кнопку.
        button_5 = telebot.types.KeyboardButton(f'{buttons_1[4]}')  # Создаём кнопку.
        button_6 = telebot.types.KeyboardButton(f'{buttons_1[5]}')  # Создаём кнопку.
        button_7 = telebot.types.KeyboardButton(f'{buttons_1[6]}')  # Создаём кнопку.
        button_8 = telebot.types.KeyboardButton(f'{buttons_1[7]}')  # Создаём кнопку.
        button_9 = telebot.types.KeyboardButton(f'{buttons_1[8]}')  # Создаём кнопку.
        keyboard.add(button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9) # Добавляем в клавиатуру keyboard все кнопки button.
        
        button = 0 # Обнуляем переменную.
        i = 0 # Добавлям счётчик для проверки на ничью.
        while button == 0: # Цикл для проверки на ничью
            try:
                button = int(buttons_1[i]) # Если buttons_1[i] не может быть числом, то увеличиваем счётчик на +1.
            except:
                if i < 9:
                    i += 1
                else:
                    break # Выходим из цикла как только счётчик дойдёт до 9.
        if button == 0: # Если за время проверки button так и остался 0, то это ничья.
            send_message = f'Ничья!' # К переменной send_message присваиваем сообщение для дальнейшего вывода.
            draw = 1 # К переменной draw присваиваем 1 ,так как игры была в ничью.
            tok.send_message(message.chat.id, send_message) # Выводим сообщения пользователя "Ничья!".
            log.logger('Ничья!', 'ответ бота') # Запускаем логгер.
            for i in range(9): # Данным циклом обнуляем все кнопки до первоначального значения.
                buttons_1[i] = str(i + 1) # Каждой кнопке присваиваем начальное значение.
            keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 3) # Данный способ создания клавиатуры в телеграмм, где row_width это ширина поля.
            button_1 = telebot.types.KeyboardButton(f'{buttons_1[0]}') # Создаём кнопку.
            button_2 = telebot.types.KeyboardButton(f'{buttons_1[1]}') # Создаём кнопку.
            button_3 = telebot.types.KeyboardButton(f'{buttons_1[2]}') # Создаём кнопку.
            button_4 = telebot.types.KeyboardButton(f'{buttons_1[3]}') # Создаём кнопку.
            button_5 = telebot.types.KeyboardButton(f'{buttons_1[4]}') # Создаём кнопку.
            button_6 = telebot.types.KeyboardButton(f'{buttons_1[5]}') # Создаём кнопку.
            button_7 = telebot.types.KeyboardButton(f'{buttons_1[6]}') # Создаём кнопку.
            button_8 = telebot.types.KeyboardButton(f'{buttons_1[7]}') # Создаём кнопку.
            button_9 = telebot.types.KeyboardButton(f'{buttons_1[8]}') # Создаём кнопку.
            keyboard.add(button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9) # Добавляем в клавиатуру keyboard все кнопки button.
            send_message = f'Новая игра!' # К переменной send_message присваиваем сообщение для дальнейшего вывода.
            tok.send_message(message.chat.id, send_message, reply_markup = keyboard) # Выводим сообщения пользователя 'Новая игра!'.
            log.logger('Новая игра!', 'ответ бота') # Запускаем логгер.
                
        
        victory = win_combinations(buttons_1) # Проверяем выигрыш человека через функцию win_combinations(), куда добавляем buttons_1 с изменёнными кнопками.
        if victory: # Если вернулось True из функции win_combinations(), то проваливаемся в if.
            send_message = f'Вы выиграли!' # К переменной send_message присваиваем сообщение для дальнейшего вывода.
            tok.send_message(message.chat.id, send_message) # Выводим сообщения пользователя 'Вы выиграли!'.
            log.logger('Вы выиграли!', 'ответ бота') # Запускаем логгер.
            for i in range(9): # Данным циклом обнуляем все кнопки до первоначального значения.
                buttons_1[i] = str(i + 1) # Каждой кнопке присваиваем начальное значение.
            for j in buttons_2: # Данным циклом обнуляем все кнопки до первоначального значения.
                j = str(i + 1) # Каждой кнопке присваиваем начальное значение.
            keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 3) # Данный способ создания клавиатуры в телеграмм, где row_width это ширина поля.
            button_1 = telebot.types.KeyboardButton(f'{buttons_1[0]}') # Создаём кнопку.
            button_2 = telebot.types.KeyboardButton(f'{buttons_1[1]}') # Создаём кнопку.
            button_3 = telebot.types.KeyboardButton(f'{buttons_1[2]}') # Создаём кнопку.
            button_4 = telebot.types.KeyboardButton(f'{buttons_1[3]}') # Создаём кнопку.
            button_5 = telebot.types.KeyboardButton(f'{buttons_1[4]}') # Создаём кнопку.
            button_6 = telebot.types.KeyboardButton(f'{buttons_1[5]}') # Создаём кнопку.
            button_7 = telebot.types.KeyboardButton(f'{buttons_1[6]}') # Создаём кнопку.
            button_8 = telebot.types.KeyboardButton(f'{buttons_1[7]}') # Создаём кнопку.
            button_9 = telebot.types.KeyboardButton(f'{buttons_1[8]}') # Создаём кнопку.
            keyboard.add(button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9) # Добавляем в клавиатуру keyboard все кнопки button.
            send_message = f'Новая игра!' # К переменной send_message присваиваем сообщение для дальнейшего вывода.
            tok.send_message(message.chat.id, send_message, reply_markup = keyboard) # Выводим сообщения пользователя 'Новая игра!'.
            log.logger('Новая игра!', 'ответ бота') # Запускаем логгер.

        else: # Проверяем выигрыш бота когда из функции win_combinations(), вернулось False.
            if draw == 0: # проверка, если предыдущая партия закончилась ничьей
                button = int(choice(buttons_2)) # Вытягиваем случайное число из  списка buttons_2.
                log.logger(button, 'ходит бот') # Запускаем логгер.
                if str(buttons_1[button - 1]) in buttons_2:
                    for i in range(len(buttons_2)):
                        if str(buttons_1[button - 1]) == buttons_2[i]:
                            counter_1 = i
                            counter_2 = 1
                if counter_2:
                    buttons_2.pop(counter_1)
                buttons_1[button - 1] = 'O' # В списке меняем элементы на нужные нам значения, например 'O'.
                keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 3) # Данный способ создания клавиатуры в телеграмм, где row_width это ширина поля.
                button_1 = telebot.types.KeyboardButton(f'{buttons_1[0]}') # Создаём кнопку.
                button_2 = telebot.types.KeyboardButton(f'{buttons_1[1]}') # Создаём кнопку.
                button_3 = telebot.types.KeyboardButton(f'{buttons_1[2]}') # Создаём кнопку.
                button_4 = telebot.types.KeyboardButton(f'{buttons_1[3]}') # Создаём кнопку.
                button_5 = telebot.types.KeyboardButton(f'{buttons_1[4]}') # Создаём кнопку.
                button_6 = telebot.types.KeyboardButton(f'{buttons_1[5]}') # Создаём кнопку.
                button_7 = telebot.types.KeyboardButton(f'{buttons_1[6]}') # Создаём кнопку.
                button_8 = telebot.types.KeyboardButton(f'{buttons_1[7]}') # Создаём кнопку.
                button_9 = telebot.types.KeyboardButton(f'{buttons_1[8]}') # Создаём кнопку.
                keyboard.add(button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9) # Добавляем в клавиатуру keyboard все кнопки button.
                victory = win_combinations(buttons_1) # Проверяем выигрыш бота через функцию win_combinations(), куда добавляем buttons_1 с изменёнными кнопками.
                if victory: # Если вернулось True из функции win_combinations(), то проваливаемся в if.
                    send_message = f'Выиграл бот!' # К переменной send_message присваиваем сообщение для дальнейшего вывода.
                    tok.send_message(message.chat.id, send_message) # Выводим сообщения пользователя 'Выиграл бот!'.
                    log.logger('Вы выиграли!', 'ответ бота') # Запускаем логгер.
                    for i in range(9): # Данным циклом обнуляем все кнопки до первоначального значения.
                        buttons_1[i] = str(i + 1) # Каждой кнопке присваиваем начальное значение.
                    for j in buttons_2: # Данным циклом обнуляем все кнопки до первоначального значения.
                        j = str(i + 1) # Каждой кнопке присваиваем начальное значение.
                    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 3) # Данный способ создания клавиатуры в телеграмм, где row_width это ширина поля.
                    button_1 = telebot.types.KeyboardButton(f'{buttons_1[0]}') # Создаём кнопку.
                    button_2 = telebot.types.KeyboardButton(f'{buttons_1[1]}') # Создаём кнопку.
                    button_3 = telebot.types.KeyboardButton(f'{buttons_1[2]}') # Создаём кнопку.
                    button_4 = telebot.types.KeyboardButton(f'{buttons_1[3]}') # Создаём кнопку.
                    button_5 = telebot.types.KeyboardButton(f'{buttons_1[4]}') # Создаём кнопку.
                    button_6 = telebot.types.KeyboardButton(f'{buttons_1[5]}') # Создаём кнопку.
                    button_7 = telebot.types.KeyboardButton(f'{buttons_1[6]}') # Создаём кнопку.
                    button_8 = telebot.types.KeyboardButton(f'{buttons_1[7]}') # Создаём кнопку.
                    button_9 = telebot.types.KeyboardButton(f'{buttons_1[8]}') # Создаём кнопку.
                    keyboard.add(button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9) # Добавляем в клавиатуру keyboard все кнопки button.
                    send_message = f'Новая игра' # К переменной send_message присваиваем сообщение для дальнейшего вывода.
                    tok.send_message(message.chat.id, send_message, reply_markup = keyboard) # Выводим сообщения пользователя 'Новая игра'.
                    log.logger('Новая игра!', 'ответ бота') # Запускаем логгер.
                send_message = f'Следующий ход' # если никакие проверки на выигрыш или ничью не прошли, делается следующий ход
                tok.send_message(message.chat.id, send_message, reply_markup = keyboard) # Выводим сообщения пользователя 'Новая игра!'.
                log.logger('Следующий ход', 'ходит следующий') # Запускаем логгер.

    else: # Если введённое пользователем не соответсвеут необходимой цифре, выводим сообщение о повторе ввода.
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 3) # Данный способ создания клавиатуры в телеграмм, где row_width это ширина поля.
        button_1 = telebot.types.KeyboardButton(f'{buttons_1[0]}') # Создаём кнопку.
        button_2 = telebot.types.KeyboardButton(f'{buttons_1[1]}') # Создаём кнопку.
        button_3 = telebot.types.KeyboardButton(f'{buttons_1[2]}') # Создаём кнопку.
        button_4 = telebot.types.KeyboardButton(f'{buttons_1[3]}') # Создаём кнопку.
        button_5 = telebot.types.KeyboardButton(f'{buttons_1[4]}') # Создаём кнопку.
        button_6 = telebot.types.KeyboardButton(f'{buttons_1[5]}') # Создаём кнопку.
        button_7 = telebot.types.KeyboardButton(f'{buttons_1[6]}') # Создаём кнопку.
        button_8 = telebot.types.KeyboardButton(f'{buttons_1[7]}') # Создаём кнопку.
        button_9 = telebot.types.KeyboardButton(f'{buttons_1[8]}') # Создаём кнопку.
        keyboard.add(button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9) # Добавляем в клавиатуру keyboard все кнопки button.
        send_message = f'Нажми, пожалуйста на неиспользованную кнопку или введите соответствующий номер кнопки.' # К переменной send_message присваиваем сообщение для дальнейшего вывода.
        tok.send_message(message.chat.id, send_message, reply_markup = keyboard) # Выводим сообщения пользователя 'Новая игра'.
        log.logger('Нажми, пожалуйста на неиспользованную кнопку или введите соответствующий номер кнопки.', 'Сообщение об ошибки') # Запускаем логгер.

tok.polling(non_stop = True) # Зацикливаем бота.