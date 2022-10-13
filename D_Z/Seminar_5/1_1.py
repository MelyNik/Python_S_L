# Напишите программу, удаляющую из текста все слова, содержащие "абв".
# В тексте используется разделитель пробел.
# Пример:
# in
# Number of words: 10
#
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба
#
# in
# Number of words: 6
#
# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва
#
# in
# Number of words: -1
#
# out
# The data is incorrect

from random import sample


def Random_text(size, text='абв'):
    result_text = []
    for i in range(size):
        # Выборка случайных букв из переменной абв в случайном порядке в количестве 3 создав список.
        result = sample(text, 3)
        # Добавили в список result_text элемент преобразованный в строку командой ''.join(result)
        result_text.append(''.join(result))
        # где '' указывает на отсутствие расстояния между элементами предыдущего списка.
    # Возвращаем список преобразовав его просто в текст с разрывом в пробел ' '.
    return ' '.join(result_text)


text = Random_text(int(input('Введите длину списка: ')))
print(text)


def Sorting_text(text):
    # Командой replace('абв', '') убрали абв и командой split() создали список с
    return ' '.join(text.replace('абв', '').split())

    # разделяющими элементы пробелами, далее преобразовали список в текст разделив пробелами ' '.join
print(Sorting_text(text))
