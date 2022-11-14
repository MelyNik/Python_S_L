import comp

def numbers(numbers):
    if len(numbers) >= 2:
        a = numbers[0]
        b = numbers[1]
        while type(a) != float:
            try:
                a = float(a)
            except:
                a = False
        while type(b) != float:
            try:
                b = float(b)
            except:
                b = False
    else:
        a = False
        b = False
    return a, b

def root(numbers):
    a = numbers[0]
    while type(a) != float:
        try:
            a = float(a)
        except:
            a = False
    return a

def complex_numbers(numbers):
    if len(numbers) >= 4:
        comp_1_1 = numbers[0]
        comp_1_2 = numbers[1]
        comp_2_1 = numbers[2]
        comp_2_2 = numbers[3]
        while type(comp_1_1) != float and type(comp_1_2) != float and type(comp_2_1) != float and type(comp_2_2) != float:
            try:
                comp_1_1 = float(comp_1_1)
                comp_1_2 = float(comp_1_2)
                comp_2_1 = float(comp_2_1)
                comp_2_2 = float(comp_2_2)
            except:
                comp_1_1 = False
                comp_1_2 = False
                comp_2_1 = False
                comp_2_2 = False
    else:
        comp_1_1 = False
        comp_1_2 = False
        comp_2_1 = False
        comp_2_2 = False
    if comp_1_1 != 0 and comp_1_2 != 0 and comp_2_1 != 0 and comp_2_2 != 0:
        number_1 = comp.comp(comp_1_1, comp_1_2)
        number_2 = comp.comp(comp_2_1, comp_2_2)
    else:
        number_1 = False
        number_2 = False
    return number_1, number_2

def complex_degree(numbers):
    if len(numbers) >= 3:
        comp_1_1 = numbers[0]
        comp_1_2 = numbers[1]
        number_2 = numbers[2]
        while type(comp_1_1) != float and type(comp_1_2) != float and type(number_2) != float:
            try:
                comp_1_1 = float(comp_1_1)
                comp_1_2 = float(comp_1_2)
                number_2 = float(number_2)
            except:
                comp_1_1 = False
                comp_1_2 = False
                number_2 = False
    else:
        comp_1_1 = False
        comp_1_2 = False
        number_2 = False
    if comp_1_1 != 0 and comp_1_2 != 0 and number_2 != 0:
        number_1 = comp.comp(comp_1_1, comp_1_2)
    else:
        number_1 = False
        number_2 = False
    return number_1, number_2

def complex_root(numbers):
    if len(numbers) >= 2:
        comp_1_1 = numbers[0]
        comp_1_2 = numbers[1]
        while type(comp_1_1) != float and type(comp_1_2) != float:
            try:
                comp_1_1 = float(comp_1_1)
                comp_1_2 = float(comp_1_2)
            except:
                comp_1_1 = False
                comp_1_2 = False
    else:
        comp_1_1 = False
        comp_1_2 = False
    if comp_1_1 != 0 and comp_1_2 != 0:
        a = comp.comp(comp_1_1, comp_1_2)
    else:
        a = False
    return a