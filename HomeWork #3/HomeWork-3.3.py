def my_func(arg1, arg2, arg3):
    max1 = max(arg1, arg2)
    if arg1 < arg2:
        max2 = max(arg1, arg3)
    else:
        max2 = max(arg2, arg3)
    print(max1 + max2)


my_func(int(input("Enter 1st argument: ")),
        int(input("Enter 2nd argument: ")),
        int(input("Enter 3rd argument: ")))
