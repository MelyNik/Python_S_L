import telebot
from telebot import types

import compl
import degree
import division_without_remainder
import division
import multiplication
import remainder_of_division
import subtraction
import summa
import logging

logging.basicConfig(level = logging.debug,
                    format = '%(asctime)s - %(levelname)s - %(message)s',
                    filename = 'Pyton_S_L\D_Z\Seminar_10\logger.log', encoding = 'utf-8')

tok = telebot.TeleBot("5704215037:AAFtYNTzAF4Y0_D4XPlOH8NWU1VlEbNojwQ")


@tok.message_handler(commands = ['start'])
def start_message(message):
    logging.debug('Start bot')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    button_1 = types.KeyboardButton(f'/Рациональные_числа')
    button_2 = types.KeyboardButton(f'/Комплексные числа')
    keyboard.add(button_1, button_2)
    send_message = f'Привет, {message.from_user.first_name}. Добро пожаловать в бот-калькулятор! С какими числами будем работать?'
    tok.send_message(message.chat.id, send_message, reply_markup = keyboard)


@tok.message_handler(commands = ['Рациональные_числа'])
def rational_numbers(message):
    logging.debug(f'{message.from_user.first_name} -- {message.from_user.id} -- Рациональные_числа')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
    button_1 = types.KeyboardButton(f'/Сумма')
    button_2 = types.KeyboardButton(f'/Вычитание')
    button_3 = types.KeyboardButton(f'/Умножение')
    button_4 = types.KeyboardButton(f'/Cтепень')
    button_5 = types.KeyboardButton(f'/Извлечение_корня')
    button_6 = types.KeyboardButton(f'/Деление')
    button_7 = types.KeyboardButton(f'/Целочисленное_деление')
    button_8 = types.KeyboardButton(f'/Остаток_от_деления')
    keyboard.add(button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8)
    send_message = f'Выберите необходимое действие.'
    tok.send_message(message.chat.id, send_message, reply_markup = keyboard)


@tok.message_handler(commands = ['Сумма'])
def summa(message):
    logging.debug(f'{message.from_user.first_name} -- {message.from_user.id} -- Сумма')
    global action
    action = message.text.split()
    keyboard = types.ForceReply(selective = True)
    send_message = f'Введи 2 числа через пробел'
    tok.send_message(message.chat.id, send_message, reply_markup = keyboard)


@tok.message_handler(commands = ['Вычитание'])
def summa(message):
    logging.debug(f'{message.from_user.first_name} -- {message.from_user.id} -- Вычитание')
    global action
    action = message.text.split()
    keyboard = types.ForceReply(selective = True)
    send_message = f'Введи 2 числа через пробел'
    tok.send_message(message.chat.id, send_message, reply_markup=keyboard)


@tok.message_handler(commands=['Целочисленное_деление'])
def summa(message):
    logging.debug(f'{message.from_user.first_name} -- {message.from_user.id} -- Целочисленное_деление')
    global action
    action = message.text.split()
    keyboard = types.ForceReply(selective=True)
    send_message = f'Введи 2 числа через пробел'
    tok.send_message(message.chat.id, send_message, reply_markup=keyboard)


@tok.message_handler(commands=['Умножение'])
def summa(message):
    logging.debug(f'{message.from_user.first_name} -- {message.from_user.id} -- Умножение')
    global action
    action = message.text.split()
    keyboard = types.ForceReply(selective=True)
    send_message = f'Введи 2 числа через пробел'
    tok.send_message(message.chat.id, send_message, reply_markup=keyboard)


@tok.message_handler(commands=['Деление'])
def summa(message):
    logging.debug(f'{message.from_user.first_name} -- {message.from_user.id} -- Деление')
    global action
    action = message.text.split()
    keyboard = types.ForceReply(selective=True)
    send_message = f'Введи 2 числа через пробел'
    tok.send_message(message.chat.id, send_message, reply_markup=keyboard)


@tok.message_handler(commands=['Остаток_от_деления'])
def summa(message):
    logging.debug(f'{message.from_user.first_name} -- {message.from_user.id} -- Остаток_от_деления')
    global action
    action = message.text.split()
    keyboard = types.ForceReply(selective=True)
    send_message = f'Введи 2 числа через пробел'
    tok.send_message(message.chat.id, send_message, reply_markup=keyboard)

@tok.message_handler(commands=['Извлечение_корня'])
def summa(message):
    logging.debug(f'{message.from_user.first_name} -- {message.from_user.id} -- Извлечение_корня')
    global action
    action = message.text.split()
    keyboard = types.ForceReply(selective=True)
    send_message = f'Введи 1 число'
    tok.send_message(message.chat.id, send_message, reply_markup=keyboard)


@tok.message_handler(commands=['Степень'])
def summa(message):
    logging.debug(f'{message.from_user.first_name} -- {message.from_user.id} -- Степень')
    global action
    action = message.text.split()
    keyboard = types.ForceReply(selective=True)
    send_message = f'Введи 2 числа через пробел'
    tok.send_message(message.chat.id, send_message, reply_markup=keyboard)


@tok.message_handler(content_types=['text'])
def addition(message):
    get_msg_bot = message.text.split()
    logging.debug(f'{message.from_user.first_name} -- {message.from_user.id} -- numbers = {get_msg_bot}')
    if action == ['/Сумма']:
        a = int(get_msg_bot[0])
        b = int(get_msg_bot[1])
        result = summa.summa(a, b)
        send_message = f'{a} + {b} = {result}'
        tok.send_message(message.chat.id, send_message)
        logging.debug(f'{message.from_user.first_name} -- {message.from_user.id} -- result = {result}')
        logging.debug('End bot')

    elif action == ['/Вычитание']:
        a = int(get_msg_bot[0])
        b = int(get_msg_bot[1])
        result = subtraction.subtraction(a, b)
        send_message = f'{a} - {b} = {result}'
        tok.send_message(message.chat.id, send_message)
        logging.debug(f'{message.from_user.first_name} -- {message.from_user.id} -- result = {result}')
        logging.debug('End bot')

    elif action == ['/Умножение']:
        a = int(get_msg_bot[0])
        b = int(get_msg_bot[1])
        result = multiplication.multiplication(a, b)
        send_message = f'{a} * {b} = {result}'
        tok.send_message(message.chat.id, send_message)
        logging.debug(f'{message.from_user.first_name} -- {message.from_user.id} -- result = {result}')
        logging.debug('End bot')

    elif action == ['/Степень']:
        a = int(get_msg_bot[0])
        b = int(get_msg_bot[1])
        result = degree.degree(a, b)
        send_message = f'{a} ** {b} = {result}'
        tok.send_message(message.chat.id, send_message)
        logging.debug(f'{message.from_user.first_name} -- {message.from_user.id} -- result = {result}')
        logging.debug('End bot')

    elif action == ['/Деление']:
        a = int(get_msg_bot[0])
        b = int(get_msg_bot[1])
        result = division.division(a, b)
        send_message = f'{a} / {b} = {result}'
        tok.send_message(message.chat.id, send_message)
        logging.debug(f'{message.from_user.first_name} -- {message.from_user.id} -- result = {result}')
        logging.debug('End bot')

    elif action == ['/Извлечение_корня']:
        a = int(get_msg_bot[0])
        result = a ** 0.5
        send_message = f'{a} ** 0,5 = {result}'
        tok.send_message(message.chat.id, send_message)
        logging.debug(f'{message.from_user.first_name} -- {message.from_user.id} -- result = {result}')
        logging.debug('End bot')

    elif action == ['/Целочисленное_деление']:
        a = int(get_msg_bot[0])
        b = int(get_msg_bot[1])
        result = division_without_remainder.division(a, b)
        send_message = f'{a} // {b} = {result}'
        tok.send_message(message.chat.id, send_message)
        logging.debug(f'{message.from_user.first_name} -- {message.from_user.id} -- result = {result}')
        logging.debug('End bot')

    elif action == ['/Остаток_от_деления']:
        a = int(get_msg_bot[0])
        b = int(get_msg_bot[1])
        result = remainder_of_division.rem(a, b)
        send_message = f'{a} % {b} = {result}'
        tok.send_message(message.chat.id, send_message)
        logging.debug(f'{message.from_user.first_name} -- {message.from_user.id} -- result = {result}')
        logging.debug('End bot')


tok.polling(non_stop=True)