from functools import reduce


def multi_even(prev_el, el):
    return prev_el * el


my_list = [el for el in range(100, 1001) if el % 2 == 0]
print(reduce(multi_even, my_list))
