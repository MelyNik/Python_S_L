def mistake():
    result = input()
    print(type(result))
    if type(result) != int:
        return 'Ошибка!!! Данное значение не предоставлено ко вводу!'

