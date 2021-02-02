from itertools import count, cycle


# a
def gen_int_from_n(n, till=10):
    for i in count(n):
        if i > till:
            return
        print(i, end=" ")


# b
def gen_cycle_list(_list, stop=22):
    cnt = 0
    for i in cycle(_list):
        if cnt == stop:
            return
        print(i, end="")
        cnt += 1


my_list = list("Mom washed the frame. ")

gen_int_from_n(3)
print("")
gen_cycle_list(my_list)
