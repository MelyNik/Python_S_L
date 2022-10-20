def search_user():
    result = input('Введите номер телефона, имя или фамилию для поиска пользователя: ')
    with open('guide.csv', 'r', encoding='utf-8') as f_1:
        for i in f_1:
            if result in i:
                print(f'Найден пользователь: {i}')
                return i
        print('Ошибка!!! Информации по данному пользователю, нет.')
    