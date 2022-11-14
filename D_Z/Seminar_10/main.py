import telebot
from telebot import types

import exceptions
import degree
import division_without_remainder
import division
import multiplication
import remainder_of_division
import subtraction
import summa
import log

tok = telebot.TeleBot("5704215037:AAFtYNTzAF4Y0_D4XPlOH8NWU1VlEbNojwQ")


@tok.message_handler(commands = ['start'])
def start_message(message):
    log.logger(message.text.split(), 'Активация бота')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    button_1 = types.KeyboardButton(f'/Рациональные_числа')
    button_2 = types.KeyboardButton(f'/Комплексные_числа')
    keyboard.add(button_1, button_2)
    send_message = f'Привет, {message.from_user.first_name}. Добро пожаловать в бот-калькулятор! С какими числами будем работать?'
    tok.send_message(message.chat.id, send_message, reply_markup = keyboard)
    log.logger('Привет, {message.from_user.first_name}. Добро пожаловать в бот-калькулятор! С какими числами будем работать?', 
    'Вывод сообщения пользователю')











@tok.message_handler(commands = ['Рациональные_числа'])
def rational_numbers(message):
    log.logger(message.text.split(), 'Выбрал пользователь')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
    button_1 = types.KeyboardButton(f'/Сумма')
    button_2 = types.KeyboardButton(f'/Вычитание')
    button_3 = types.KeyboardButton(f'/Умножение')
    button_4 = types.KeyboardButton(f'/Деление')
    button_5 = types.KeyboardButton(f'/Корень')
    button_6 = types.KeyboardButton(f'/Степень')
    button_7 = types.KeyboardButton(f'/Целочисленное_деление')
    button_8 = types.KeyboardButton(f'/Остаток_от_деления')
    keyboard.add(button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8)
    send_message = f'Выберите действие!'
    tok.send_message(message.chat.id, send_message, reply_markup = keyboard)
    log.logger(send_message, 'Вывод сообщения пользователю')







@tok.message_handler(commands = ['Комплексные_числа'])
def rational_numbers(message):
    log.logger(message.text.split(), 'Выбрал пользователь')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
    button_1 = types.KeyboardButton(f'/Сумма_комплексных_чисел')
    button_2 = types.KeyboardButton(f'/Вычитание_комплексных_чисел')
    button_3 = types.KeyboardButton(f'/Умножение_комплексных_чисел')
    button_4 = types.KeyboardButton(f'/Деление_комплексных_чисел')
    button_5 = types.KeyboardButton(f'/Корень_комплексных_чисел')
    button_6 = types.KeyboardButton(f'/Степень_комплексных_чисел')
    keyboard.add(button_1, button_2, button_3, button_4, button_5, button_6)
    send_message = f'Выберите действие!'
    tok.send_message(message.chat.id, send_message, reply_markup = keyboard)
    log.logger(send_message, 'Вывод сообщения пользователю')












@tok.message_handler(commands = ['Сумма_комплексных_чисел'])
def process(message):
    log.logger(message.text.split(), 'Выбрал пользователь')
    global data
    data = message.text.split()
    keyboard = types.ForceReply(selective = True)
    send_message = f'Введи через пробел всего 4 числа. В первую очередь действительную\
 и мнимую части 1-го комплексного числа, далее действительную и мнимую части 2-го\
 комплексного числа.'
    tok.send_message(message.chat.id, send_message, reply_markup = keyboard)
    log.logger(send_message, 'Вывод сообщения пользователю')

@tok.message_handler(commands = ['Вычитание_комплексных_чисел'])
def process(message):
    log.logger(message.text.split(), 'Выбрал пользователь')
    global data
    data = message.text.split()
    keyboard = types.ForceReply(selective = True)
    send_message = f'Введи через пробел всего 4 числа. В первую очередь действительную\
 и мнимую части 1-го комплексного числа, далее действительную и мнимую части 2-го\
 комплексного числа.'
    tok.send_message(message.chat.id, send_message, reply_markup = keyboard)
    log.logger(send_message, 'Вывод сообщения пользователю')

@tok.message_handler(commands = ['Умножение_комплексных_чисел'])
def process(message):
    log.logger(message.text.split(), 'Выбрал пользователь')
    global data
    data = message.text.split()
    keyboard = types.ForceReply(selective = True)
    send_message = f'Введи через пробел всего 4 числа. В первую очередь действительную\
 и мнимую части 1-го комплексного числа, далее действительную и мнимую части 2-го\
 комплексного числа.'
    tok.send_message(message.chat.id, send_message, reply_markup = keyboard)
    log.logger(send_message, 'Вывод сообщения пользователю')

@tok.message_handler(commands = ['Деление_комплексных_чисел'])
def process(message):
    log.logger(message.text.split(), 'Выбрал пользователь')
    global data
    data = message.text.split()
    keyboard = types.ForceReply(selective = True)
    send_message = f'Введи через пробел всего 4 числа. В первую очередь действительную\
 и мнимую части 1-го комплексного числа, далее действительную и мнимую части 2-го\
 комплексного числа.'
    tok.send_message(message.chat.id, send_message, reply_markup = keyboard)
    log.logger(send_message, 'Вывод сообщения пользователю')

@tok.message_handler(commands = ['Корень_комплексных_чисел'])
def process(message):
    log.logger(message.text.split(), 'Выбрал пользователь')
    global data
    data = message.text.split()
    keyboard = types.ForceReply(selective = True)
    send_message = f'Введи через пробел всего 2 числа. В первую очередь действительную часть,\
 далее мнимую часть комплексного числа.'
    tok.send_message(message.chat.id, send_message, reply_markup = keyboard)
    log.logger(send_message, 'Вывод сообщения пользователю')

@tok.message_handler(commands = ['Степень_комплексных_чисел'])
def process(message):
    log.logger(message.text.split(), 'Выбрал пользователь')
    global data
    data = message.text.split()
    keyboard = types.ForceReply(selective = True)
    send_message = f'Введи через пробел всего 3 числа. В первую очередь действительную часть,\
 и мнимую часть комплексного числа, далее степень возведения.'
    tok.send_message(message.chat.id, send_message, reply_markup = keyboard)
    log.logger(send_message, 'Вывод сообщения пользователю')











@tok.message_handler(commands = ['Сумма'])
def process(message):
    log.logger(message.text.split(), 'Выбрал пользователь')
    global data
    data = message.text.split()
    keyboard = types.ForceReply(selective = True)
    send_message = f'Введи 2 числа через пробел.'
    tok.send_message(message.chat.id, send_message, reply_markup = keyboard)
    log.logger(send_message, 'Вывод сообщения пользователю')

@tok.message_handler(commands = ['Вычитание'])
def process(message):
    log.logger(message.text.split(), 'Выбрал пользователь')
    global data
    data = message.text.split()
    keyboard = types.ForceReply(selective = True)
    send_message = f'Введи 2 числа через пробел.'
    tok.send_message(message.chat.id, send_message, reply_markup=keyboard)
    log.logger(send_message, 'Вывод сообщения пользователю')

@tok.message_handler(commands=['Умножение'])
def process(message):
    log.logger(message.text.split(), 'Выбрал пользователь')
    global data
    data = message.text.split()
    keyboard = types.ForceReply(selective=True)
    send_message = f'Введи 2 числа через пробел.'
    tok.send_message(message.chat.id, send_message, reply_markup=keyboard)
    log.logger(send_message, 'Вывод сообщения пользователю')

@tok.message_handler(commands=['Деление'])
def process(message):
    log.logger(message.text.split(), 'Выбрал пользователь')
    global data
    data = message.text.split()
    keyboard = types.ForceReply(selective=True)
    send_message = f'Введи 2 числа через пробел.'
    tok.send_message(message.chat.id, send_message, reply_markup=keyboard)
    log.logger(send_message, 'Вывод сообщения пользователю')

@tok.message_handler(commands=['Корень'])
def process(message):
    log.logger(message.text.split(), 'Выбрал пользователь')
    global data
    data = message.text.split()
    keyboard = types.ForceReply(selective=True)
    send_message = f'Введи 1 число.'
    tok.send_message(message.chat.id, send_message, reply_markup=keyboard)
    log.logger(send_message, 'Вывод сообщения пользователю')

@tok.message_handler(commands=['Степень'])
def process(message):
    log.logger(message.text.split(), 'Выбрал пользователь')
    global data
    data = message.text.split()
    keyboard = types.ForceReply(selective=True)
    send_message = f'Введи 2 числа через пробел.'
    tok.send_message(message.chat.id, send_message, reply_markup=keyboard)
    log.logger(send_message, 'Вывод сообщения пользователю')

@tok.message_handler(commands=['Целочисленное_деление'])
def process(message):
    log.logger(message.text.split(), 'Выбрал пользователь')
    global data
    data = message.text.split()
    keyboard = types.ForceReply(selective=True)
    send_message = f'Введи 2 числа через пробел.'
    tok.send_message(message.chat.id, send_message, reply_markup=keyboard)
    log.logger(send_message, 'Вывод сообщения пользователю')

@tok.message_handler(commands=['Остаток_от_деления'])
def process(message):
    log.logger(message.text.split(), 'Выбрал пользователь')
    global data
    data = message.text.split()
    keyboard = types.ForceReply(selective=True)
    send_message = f'Введи 2 числа через пробел.'
    tok.send_message(message.chat.id, send_message, reply_markup=keyboard)
    log.logger(send_message, 'Вывод сообщения пользователю')








@tok.message_handler(content_types=['text'])
def result(message):
    get_message = message.text.split()
    log.logger(get_message, 'Ввёл пользователь')










    if data == ['/Сумма_комплексных_чисел']:
        number_1, number_2 = exceptions.complex_numbers(get_message)
        if number_1 == False and number_2 == False:
            send_message = 'Ошибка! Повторите ввод.'
            tok.send_message(message.chat.id, send_message)
        else:
            result = summa.summa(number_1, number_2)
            send_message = f'{number_1} + {number_2} = {result}'
            tok.send_message(message.chat.id, send_message)
        log.logger(send_message, 'Вывод сообщения пользователю')
    
    elif data == ['/Вычитание_комплексных_чисел']:
        number_1, number_2 = exceptions.complex_numbers(get_message)
        if number_1 == False and number_2 == False:
            send_message = 'Ошибка! Повторите ввод.'
            tok.send_message(message.chat.id, send_message)
        else:
            result = subtraction.subtraction(number_1, number_2)
            send_message = f'{number_1} - {number_2} = {result}'
            tok.send_message(message.chat.id, send_message)
        log.logger(send_message, 'Вывод сообщения пользователю')

    elif data == ['/Умножение_комплексных_чисел']:
        number_1, number_2 = exceptions.complex_numbers(get_message)
        if number_1 == False and number_2 == False:
            send_message = 'Ошибка! Повторите ввод.'
            tok.send_message(message.chat.id, send_message)
        else:
            result = multiplication.multiplication(number_1, number_2)
            send_message = f'{number_1} * {number_2} = {result}'
            tok.send_message(message.chat.id, send_message)
        log.logger(send_message, 'Вывод сообщения пользователю')

    elif data == ['/Деление_комплексных_чисел']:
        number_1, number_2 = exceptions.complex_numbers(get_message)
        if number_1 == False and number_2 == False:
            send_message = 'Ошибка! Повторите ввод.'
            tok.send_message(message.chat.id, send_message)
        else:
            result = division.division(number_1, number_2)
            send_message = f'{number_1} / {number_2} = {result}'
            tok.send_message(message.chat.id, send_message)
        log.logger(send_message, 'Вывод сообщения пользователю')

    elif data == ['/Корень_комплексных_чисел']:
        number_1 = exceptions.complex_root(get_message)
        if number_1 == False:
            send_message = 'Ошибка! Повторите ввод.'
            tok.send_message(message.chat.id, send_message)
        else:
            result = degree.degree(number_1, 0.5)
            send_message = f'{number_1} ** 0.5 = {result}'
            tok.send_message(message.chat.id, send_message)
        log.logger(send_message, 'Вывод сообщения пользователю')

    elif data == ['/Степень_комплексных_чисел']:
        number_1, number_2 = exceptions.complex_degree(get_message)
        if number_1 == False and number_2 == False:
            send_message = 'Ошибка! Повторите ввод.'
            tok.send_message(message.chat.id, send_message)
        else:
            result = degree.degree(number_1, number_2)
            send_message = f'{number_1} ** {number_2} = {result}'
            tok.send_message(message.chat.id, send_message)
        log.logger(send_message, 'Вывод сообщения пользователю')









    elif data == ['/Сумма']:
        number_1, number_2 = exceptions.numbers(get_message)
        if number_1 == False and number_2 == False:
            send_message = 'Ошибка! Повторите ввод.'
            tok.send_message(message.chat.id, send_message)
        else:
            result = summa.summa(number_1, number_2)
            send_message = f'{number_1} + {number_2} = {result}'
            tok.send_message(message.chat.id, send_message)
        log.logger(send_message, 'Вывод сообщения пользователю')

    elif data == ['/Вычитание']:
        number_1, number_2 = exceptions.numbers(get_message)
        if number_1 == False and number_2 == False:
            send_message = 'Ошибка! Повторите ввод.'
            tok.send_message(message.chat.id, send_message)
        else:
            result = subtraction.subtraction(number_1, number_2)
            send_message = f'{number_1} - {number_2} = {result}'
            tok.send_message(message.chat.id, send_message)
        log.logger(send_message, 'Вывод сообщения пользователю')

    elif data == ['/Умножение']:
        number_1, number_2 = exceptions.numbers(get_message)
        if number_1 == False and number_2 == False:
            send_message = 'Ошибка! Повторите ввод.'
            tok.send_message(message.chat.id, send_message)
        else:
            result = multiplication.multiplication(number_1, number_2)
            send_message = f'{number_1} * {number_2} = {result}'
            tok.send_message(message.chat.id, send_message)
        log.logger(send_message, 'Вывод сообщения пользователю')

    elif data == ['/Деление']:
        number_1, number_2 = exceptions.numbers(get_message)
        if number_1 == False and number_2 == False:
            send_message = 'Ошибка! Повторите ввод.'
            tok.send_message(message.chat.id, send_message)
        else:
            result = division.division(number_1, number_2)
            send_message = f'{number_1} / {number_2} = {result}'
            tok.send_message(message.chat.id, send_message)
        log.logger(send_message, 'Вывод сообщения пользователю')

    elif data == ['/Корень']:
        number_1 = exceptions.root(get_message)
        if number_1 == False:
            send_message = 'Ошибка! Повторите ввод.'
            tok.send_message(message.chat.id, send_message)
        else:
            result = degree.degree(number_1, 0.5)
            send_message = f'{number_1} ** 0.5 = {result}'
            tok.send_message(message.chat.id, send_message)
        log.logger(send_message, 'Вывод сообщения пользователю')

    elif data == ['/Степень']:
        number_1, number_2 = exceptions.numbers(get_message)
        if number_1 == False and number_2 == False:
            send_message = 'Ошибка! Повторите ввод.'
            tok.send_message(message.chat.id, send_message)
        else:
            result = degree.degree(number_1, number_2)
            send_message = f'{number_1} ** {number_2} = {result}'
            tok.send_message(message.chat.id, send_message)
        log.logger(send_message, 'Вывод сообщения пользователю')

    elif data == ['/Целочисленное_деление']:
        number_1, number_2 = exceptions.numbers(get_message)
        if number_1 == False and number_2 == False:
            send_message = 'Ошибка! Повторите ввод.'
            tok.send_message(message.chat.id, send_message)
        else:
            result = division_without_remainder.division(number_1, number_2)
            send_message = f'{number_1} // {number_2} = {result}'
            tok.send_message(message.chat.id, send_message)
        log.logger(send_message, 'Вывод сообщения пользователю')

    elif data == ['/Остаток_от_деления']:
        number_1, number_2 = exceptions.numbers(get_message)
        if number_1 == False and number_2 == False:
            send_message = 'Ошибка! Повторите ввод.'
            tok.send_message(message.chat.id, send_message)
        else:
            result = remainder_of_division.rem(number_1, number_2)
            send_message = f'{number_1} % {number_2} = {result}'
            tok.send_message(message.chat.id, send_message)
        log.logger(send_message, 'Вывод сообщения пользователю')

    send_msg = f'Для нового запуска калькулятора введите команду /start'
    tok.send_message(message.chat.id, send_msg)




tok.polling(non_stop=True)