#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = my_list.copy()
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            result[i] = True
        else:
            result[i] = False
    return result
