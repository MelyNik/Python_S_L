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

def Random_text(size, text = 'абв'):
    result_text = []
    for i in range(size):
        result = sample(text, 3) # Выборка случайных букв из переменной абв в случайном порядке в количестве 3 создав список.
        result_text.append(''.join(result)) # Добавили в список result_text элемент преобразованный в строку командой ''.join(result)
        # где '' указывает на отсутствие расстояния между элементами предыдущего списка.
    return ' '.join(result_text) # Возвращаем список преобразовав его просто в текст с разрывом в пробел ' '.

text = Random_text(int(input('Введите длину списка: ')))
print(text)

def Sorting_text(text):
    return ' '.join(text.replace('абв', '').split()) # Командой replace('абв', '') убрали абв и командой split() создали список с
    # разделяющими элементы пробелами, далее преобразовали список в текст разделив пробелами ' '.join
print(Sorting_text(text))

