def my_factorial(n):
    if (n == 0) or (n == 1):
        return 1

    for i in range(1, n + 1):
        if i == 1:
            cnt = 1
        cnt *= i
        yield cnt


for el in my_factorial(10):
    print(el, end=" ")
