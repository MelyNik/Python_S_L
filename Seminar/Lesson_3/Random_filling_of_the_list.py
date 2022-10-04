import random

def Filling_in_the_list(length,mi, ma):
    my_list = list(range(length))
    for i in my_list:
        my_list[i] = random.randint(mi,ma)
    print(my_list)