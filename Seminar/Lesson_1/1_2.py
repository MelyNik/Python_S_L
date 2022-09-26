
# import random
# 
# a = random.randint(0,10)
# b = random.randint(0,10)
# c = random.randint(0,10)
# d = random.randint(0,10)
# e = random.randint(0,10)
# 
# max = a
# if max < b:
#     max = b
# if max < c:
#     max = c
# if max < d:
#     max = d
# if max < e:
#     max = e
# 
# print(max)
# 

import random

max = 0
for i in range(5):
    number = random.randrange(1,15)
    if max < number:
        max = number
print(max)
