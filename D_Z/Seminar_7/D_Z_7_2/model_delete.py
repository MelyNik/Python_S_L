def delete():
    with open('guide.csv', 'r', encoding='utf-8') as f_1:
        print('Введите имя, фамилию и номер телефона пользователя котрого вы хотите удалить: ')
        surname = input('Фамилия:\n').lower().replace(' ', '')
        name = input('Имя:\n').lower().replace(' ', '')
        number = input('Номер телефона:\n')
        my_list = f_1.readlines()
        counter = 1
        with open('guide.csv', 'w', encoding='utf-8') as f_2:
            for line in my_list:       
                if surname in line and name in line and number in line:
                    print('\nНайден пользователь: ' + line)
                    num = int(input('Введите 1 для подтверждения удаления или 0 для отмены: '))
                    if not num:
                        f_2.write(line)
                        print('Удаление отменено.')
                        counter = 0
                    else:
                        print('Запись удалена.')
                        counter = 0
                else:
                    f_2.write(line)
                    counter = 0              
            if counter: 
                print('Данные не найдены')
