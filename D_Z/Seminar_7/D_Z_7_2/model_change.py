def change():
    with open('guide.csv', 'r', encoding='utf-8') as f_1:
        print('Введите имя, фамилию и номер телефона пользователя котрого вы хотите изменить:')
        surname = input('Фамилия:\n').lower().replace(' ', '')
        name = input('Имя:\n').lower().replace(' ', '')
        number = input('Номер телефона:\n')
        my_list = f_1.readlines()
        counter = 1
        with open('guide.csv', 'w', encoding='utf-8') as f_2:
            for line in my_list:       
                if surname in line and name in line and number in line:
                    print('\nНайден пользователь: ' + line)
                    surname = input('Введите новую фамилию:\n').lower().replace(' ', '')
                    result = True
                    while result == True:
                        t = 0 
                        for i in range(len(surname)):
                            if surname[i].isdigit():
                                t = 1
                        if t:
                            surname = input('Фамилия содержит недопустимые значения, введите повторно:\n').lower().replace(' ', '')
                        else:
                            result = False
                    name = input('Введите новое имя:\n').lower().replace(' ', '')
                    result = True
                    while result == True:
                        t = 0 
                        for i in range(len(name)):
                            if name[i].isdigit():
                                t = 1
                        if t == 1:
                            name = input('Фамилия содержит недопустимые значения, введите повторно:\n').lower().replace(' ', '')
                        else:
                            result = False
                    number = input('Введите новый номер телефона:\n').lower().replace(' ', '')
                    while not number.isdigit():
                        number = input('Номер телефона содержит недопустимые значения, введите повторно:\n')
                    f_2.write(surname + ' ')
                    f_2.write(name + ' ')
                    f_2.write(number + '\n')
                    print()
                    print(f'Данные пользователя изменены на: {surname} {name} {number}')
                    counter = 0
                else:
                    f_2.write(line)
            if counter: 
                print('Данные не найдены')
