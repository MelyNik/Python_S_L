# Написать функцию, аргументы имена сотрудников, возвращает словарь,
# ключи — первые буквы имён, значения — списки, содержащие имена,
# начинающиеся с соответствующей буквы.
# Пример:
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
# out
# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}


def Names(*my): # "*" Означает, что в функцию через * в args мы можем передать много информации и дальше просто распоковать.
    dictionary = {} # Таким образом создали пустой словарь.
    for i in sorted(my): # Проходим по всем элементам в args, а функция sorted(), берёт в первую очередь элементы из переменной args отсортированные сверху
        # так скажем по алфавиту.
        initial = i[0] # Создали переменую initial и добавили в неё i[0], где i это сам элемента, а индекс 0 первая буква этого элемента.
        if initial not in dictionary: # Если буквы под пременной initial в словаре нет,
            dictionary[initial] = [i] # то в словарь dictionary с ключом [initial](это буква) мы присваиваем [i] слово на эту букву..
        else:
            dictionary[initial] += [i] # Иначе в словарь dictionary с ключом [initial](это буква) мы добавляем ещё одно слово с такой же буквой.
    return dictionary

print(Names("Иван", "Мария", "Петр", "Илья", "Марина", "Алина", "Бибочка"))


def Names1(*my): 
    dictionary = {} 
    for i in sorted(my): 
        initial = i[0] 
        if initial in dictionary: 
            dictionary[initial] += [i] 
        else:
            dictionary[initial] = [i]
    return dictionary

print(Names1("Иван", "Мария", "Петр", "Илья", "Марина", "Алина", "Бибочка"))





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
    if "" not in args: # "" означает если  args не пустой то проваливаемся в if.
        return {ch: list(names) for ch, names in groupby(sorted(args), key=lambda i: i[0]) if ch}
    return "Error"


print(thesaurus("Иван", "Мария", "Петр", "Илья",
      "Марина", "Петр", "Алина", "Бибочка"))


#  ________________________________________________________ 3 вариант

def thesaurus(*args):
    if "" not in args:
        return {ch[0]: list(filter(lambda el: el.startswith(ch[0]), args)) for ch in sorted(args)}
    return "Error"


print(thesaurus('Кармен', 'Андрей', 'Василий', 'Алексей', 'Дмитрий', 'Виктор', 'Инна', 'Александра', 'Игнат', 'Спартак',
          'Якоб', 'Люция', 'Дионис', 'Агора', 'Игорь'))
