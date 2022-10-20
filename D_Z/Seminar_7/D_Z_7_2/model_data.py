
def creating_a_directory():
    with open('guide.csv', 'a', encoding='utf-8') as f_1:
        surname = input('Введите фамилию: ').lower().replace(' ', '')
        result = True
        while result == True:
            t = 0 
            for i in range(len(surname)):
                if surname[i].isdigit():
                    t = 1
            if t == 1:
                surname = input('Фамилия содержит недопустимые значения, введите повторно:\n').lower().replace(' ', '')
            else:
                result = False
        result = True
        name = input('Введите имя: ').lower().replace(' ', '')
        result = True
        while result == True:
            t = 0 
            for i in range(len(name)):
                if name[i].isdigit():
                    t = 1
            if t == 1:
                name = input('Имя содержит недопустимые значения, введите повторно:\n').lower().replace(' ', '')
            else:
                result = False
        number = input('Введите номер телефона: ').lower().replace(' ', '')
        while not number.isdigit():
            number = input('Номер телефона содержит недопустимые значения, введите повторно:\n')
        f_1.write(f'{surname} {name} {number}'+'\n')
        print(f'Пользвотель {surname} {name} {number}, добавлен.')
    print()
    return f_1

