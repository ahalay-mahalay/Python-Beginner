def multi_sum(*args):
    args_sum = 0
    while True:
        args = input("Enter arguments separated by whitespaces: ").split()
        for i in args:
            if i.replace(".", "").isdigit():
                args_sum += float(i)
            else:
                print(args_sum)
                return
        print(args_sum)


multi_sum(0)
