# Напишите программу вычисления арифмитического выражения заданного строкой.
# Используйте операции +,-,/,* приоритет операций стандартный.
# * Добавьте скобки, приоритет операций меняется.
# in 2-2+7*2
# out 14
# in 2-(2+7)*2
# out -16
# in 101/2-(12+8)*3
# out -9.5

actions = {
    "^": lambda x, y: str(float(x) ** float(y)),
    "*": lambda x, y: str(float(x) * float(y)),
    "/": lambda x, y: str(float(x) / float(y)),
    "+": lambda x, y: str(float(x) + float(y)),
    "-": lambda x, y: str(float(x) - float(y))
}

def staples(text):
    array = [] # создали список. 
    i = 0 # Переменная которая будет отвечать за индекс.
    while i < len(text): # Проходим по всем элементам строки text.
        if text[i] == '(': # Идём дальше если строка text с индексом i равна скобки '('.
            m = text.index(')', i) # Данным способом мы присваиваем к переменной m индекс обратной скобки из переменной text которая попадётся первая. 
            array.append(text[i+1:m]) # Добавляем в список  array всё что попадает в промежуто от индекса i+1 до m, т.е. всё что в скобках.
            i = m # Прис
        else:
            array.append(text[i])
        i+=1
    return array

def disclosure_staples(array1): # Эта функция вычисляет выражение в скобках.
    for i in range(len(array1)):
        if isinstance(array1[i], list): # Эта функция уточняет если элемент списка array1 с индексом i является сиском list то прроваливаемся в if.
            a, b, c = staples(array1[i]) # С помощью функции staples созданной ранее мы присвоили к каждой переменной a, b, c конкретные числа.
            array1[i] = actions[b](a,c) # К элементу списка с индексом i присвоили выражения вычесленное с помщью словаря в который мы подставили цифры переменных выше.
    return array1

def result(array2):
    arr = [i for i, j in enumerate(array2) if j in '*/'] # Данным способом мы находим индексы элементов */ если они есть в списке и создаём отдельный из них списко arr.
    print(arr)
    while arr: # Если список arr не пустой, то мы проваливаемся в цикл.
        t = arr[0] # Назначаем переменной индекс первого попавшегося элемента * или / так как индекс 0 и есть первый элемент из списка.
        a, b, c = array2[t-1:t+2] # Далее к переменным a, b, c присваиваем перечень элементов списка array2 с индексем от t-1 до t+2.
        # Т.е. знак * или / в списке array2 находится по индексом 3, соответсвенно к переменной a добавим элемент до знака * или / и к переменной с добавим
        # элемент после знака * или / . Получается выражение где a(цифра) b(знак * или *) с(цифра).
        array2.insert(t-1 ,actions[b](a,c)) # И далее в место элемента до знака / или * добавляем новый элемент 
        # Который получился выражением благодоря словарю actions[b](a,c).
        # Так как командой array2.insert мы добавили новый элемент список стал выглядеть так ['2', '-', '18.0', '9.0', '*', '2', '/', '4']
        # И нам нужно удалить уже решённое вражение '9.0', '*', '2', для этого мы используем del array2[t:t+3] ниже 
        del array2[t:t+3] # где индекс начало промежудка это t(3(9)) конец промежудка t+3(5(2)) и того '9.0', '*', '2',
        # В списке осталось ['2', '-', '18.0', '/', '4']
        arr = [i for i, j in enumerate(array2) if j in '*/'] # Опять находим индекс но уже следующего знака * или / если он есть, если есть цикл запускается снова.

    while len(array2) > 1: # Если длина array2 функции больше 1 элемента то остаёмся в цикле. 
        a, b, c = array2[:3] # После того как все скобки и знаки приоритета * и / убраны решаем вырожения по порядку.
        # К переменным a, b, c присваиваем элемента с индексом от 0 до 3
        del array2[:3] # Далее заранее удалили эти элементы от 0 до 3.
        array2.insert(0 ,actions[b](a,c)) # И в индекс 0 добавили уже результат воспользовавшись словарём.
    return array2 # Выводим список тогда огда останется только 1 элемент, это и есть результат уравнения.

text = '2 - ( 2 + 7 ) * 2 / 4'

arr = staples(text.split())
print(arr) # Вывод [['10', '+', '5'], '*', '3', '-', '8']. В фнкцию уже заходит список из за split и разделяется пробелами.
# 10 одним элементом, потому, что в фукцию заходит split(), т.е. все элементы разделяются пробелами.

print(result(disclosure_staples(arr)))