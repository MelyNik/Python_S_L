# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Ссылка https://fb.ru/article/369240/algoritm-rle-opisanie-osobennosti-pravila-i-primeryi
# Пример:
# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'
#
# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ
#
# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ
#
# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q


# Самостоятельно не справился, только разобрав уже готовое.


from itertools import groupby, starmap
from os import path


def Encode(text='text.txt', final_text='text_f.txt'):
    # Проверяем наличие пути только файла text.
    if path.exists(text) and not path.exists(final_text):
        # path.exists - функция которая проверяет наличие пути у файла или его отсутствие.
        # В If Указали, что 1 файл должен существовать, а другой нет, для того, что другой файл создали, а не взяли откуда-то
        # Далее открываем оба файла для взаимодействия с ними. 
        # with open(text) без режима, потому, что по умолчанию стоит на чтении 'r'.
        with open(text) as f_1, \
                open(final_text, 'a') as f_2: # Файл final_text открыли с возможностью дозаписи "a".
            for i in f_1: # Цикл в данном случае обозначает, что i проходит по строке и каждая новая i это новая строка.
                # Ниже создали List Comprehension (быстрый список) и преобразовали его в текст командой ''.join() без пробелов.
                f_2.write(''.join([f'{len(list(l))}{letter}' for letter, l in groupby(i)]))
                # Пишем в файл f_2 функцией  groupby(i) где i это строка, letter это буква, а l это количество
                # таких же букв идущих подряд, и получилась длина списка из этих букв {len(list(l))}{letter}.
    else:
        print('The files do not exists in the system!')


def Decode(result):
    if path.exists(result): # методом path.exists(result) проверяем существует ли файл result.
        with open(result) as r: # Открываем файл result назвав его r.
            text = '' # Создаём пустую переменную текст строковую.
            for i in r: # Циклом i проходит по всем элементам файла r.
                my_list = [] # Созадём пустой список.
                for l in i.strip(): # Данным образом мы убрали все пробелы в том числе переход на новую строку
                    # что бы взаимодейстововать с файлом целиком.
                    if l.isdigit(): # Если элемент цифра, то добавляем её созданную переменную text как строку.
                        text += l
                    else:
                        my_list.append([int(text), l]) # Иначе в список my_list добавляем картеж где первое значение количество(так думаю), а второе это само значение.
                        text = '' # Обнуляем переменную.
                print(''.join(starmap(lambda x, y: x * y, my_list)))
    else:
        print('The files do not exists in the system!')


Encode(input('Enter the name of the file with the text\n'),
       input('Enter the file name to record\n'))
Decode(input('Enter the name of the file to decode\n'))
