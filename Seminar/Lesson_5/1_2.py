# Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую 
# последовательность. Порядок элементов менять нельзя.
# in 8
# out 
# [10,0,5,11,6,1,15,10]
# [[10,11,15],[0,5,11,15],[5,11,15],[11,15],[6,15],[1,15]]

from random import choices

def get_array(size):
    return choices(range(size*2) ,k = size) # Даным способом мы просто вернули готовый список
    # где choices уже создаёт сисок в который могут попасть элекменты от 0 до size*2 ( по умолчанию в range идёт от 0)
    # а длина списка будет равна size(обозначается k = size)

def new_array(array):
    new_list_1 = []
    for i in range(len(array)):
        new_list_2 = [array[i]]
        number = array[i]
        for j in range(i+1, len(array)):
            if array[j] > number :
                new_list_2.append(array[j])
                number = array[j]
        if len(new_list_2) > 1:
            new_list_1.append(new_list_2)
    return new_list_1


array = get_array(10)
print(array, new_array(array), sep='\n') # Таким способом сначало вывели список array, 
# а потом функцию new_array(array), далее воспользовались командой sep='\n' чем разделели список array
# и функцию new_array(array) новой строкой.
