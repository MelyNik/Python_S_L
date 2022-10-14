# Написать функцию, аргументы имена сотрудников, возвращает словарь,
# ключи — первые буквы имён, значения — списки, содержащие имена,
# начинающиеся с соответствующей буквы.
# Пример:
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
# out
# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}


def Names(*args):
    dictionary = {}
    for i in sorted(args):
        initial = i[0]
        if initial not in dictionary:
            dictionary[initial] = [i]
        dictionary[initial] += [i]
    return dictionary

print(Names("Иван", "Мария", "Петр", "Илья", "Марина", "Алина", "Бибочка"))








# Для себя.

#  ________________________________________________________ 1 вариант

from itertools import groupby


def thesaurus(*args):
    names_dict = {}
    for i in sorted(args):
        letter = i[0]
        if letter not in names_dict:
            names_dict[letter] = [i]
        names_dict[letter] += [i]

    return names_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Марина", "Алина", "Бибочка"))

#  ________________________________________________________ 2 вариант


def thesaurus(*args):
    if "" not in args:
        return {ch: list(names) for ch, names in groupby(sorted(args), key=lambda i: i[0]) if ch}
    return "Error"


print(thesaurus("Иван", "Мария", "Петр", "Илья",
      "Марина", "Петр", "Алина", "Бибочка"))


#  ________________________________________________________ 3 вариант

def thesaurus(*args):
    if "" not in args:
        return {ch[0]: list(filter(lambda el: el.startswith(ch[0]), args)) for ch in sorted(args)}
    return "Error"


thesaurus('Кармен', 'Андрей', 'Василий', 'Алексей', 'Дмитрий', 'Виктор', 'Инна', 'Александра', 'Игнат', 'Спартак',
          'Якоб', 'Люция', 'Дионис', 'Агора', 'Игорь')
