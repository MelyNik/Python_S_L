def conclusion():
    print('Предоставлен справочник: \n')
    with open('guide.csv', 'r', encoding='utf-8') as f_1:
        for i in f_1:
            print(i.strip())
