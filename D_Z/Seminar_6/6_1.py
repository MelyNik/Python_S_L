# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента. Use comprehension.
# Пример:
# in
# 9
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]
# in
# 10
# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

from random import sample

def Result(size):
    array = sample(range(size*2), size)
    print(array)
    return [array[i] for i in range(1,len(array)) if array[i] > array[i - 1]]

size = int(input('Введите длину списка: '))
print(Result(size))



# Для разбора

from random import randint # Принимает только 2 аргумента, не больше не меньше. randint(0, 1000)


def more_then(size):
    original_list = [randint(0, 1000) for _ in range(size)]# Данным способом мы составили случайный список.
    # А именно randint выбирает случайное число от 0 до 150 включительно.
    # for _ in range(size)- , где "_" это как "i", т.е. _ проходит по длине будущего списка size и столько раз вытягивает число из randint(0,150).
    print(original_list)
    return [num for i, num in enumerate(original_list[1:]) if num > original_list[i]]
    # for i, num in enumerate(original_list[1:]) - возвращает кортеж, где i - индекс, а num это сам элемент.
    # Принцип enumerate - i всегда индекс, т.е. каждый следующий цикл i увеличвается на + 1, а num это просто число,
    # Хитрость в том, что i всегда начинается с 0, а num от туда от куда укажем, как в случае enumerate(original_list[1:])
    # где индекс i опять же будет идти всегда с 0, а элмент будет проверять с индекса 1, т.е. сравнивать элемент с индексом i (на страте это 0) с индексом 1.
    # А так же original_list[1:] означает, что мы работаем со списком от 1 до конца.

print(more_then(int(input())))




