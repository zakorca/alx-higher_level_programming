#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len1 = len(tuple_a)
    len2 = len(tuple_b)
    if len1 < 1:
        tuple_a = (0, 0)
    elif len1 < 2:
        tuple_a = (tuple_a[0], 0)
    if len2 < 1:
        tuple_b = (0, 0)
    elif len2 < 2:
        tuple_b = (tuple_b[0], 0)
    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return result
