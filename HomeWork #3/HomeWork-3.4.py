# method #1
def pow_operator(x, y):
    return x ** y


# method #2
def pow_cycle(x, y):
    i = 0
    my_pow = 1
    while i < abs(y):
        my_pow *= x
        i += 1
    return 1 / my_pow


inputX = ""
inputY = ""

while True:
    inputX = float(input("Enter a real positive number: "))
    if inputX > 0:
        break

while True:
    inputY = int(input("Enter a negative integer: "))
    if inputY < 0:
        break

print("Method #1:", pow_operator(inputX, inputY))
print("Method #2:", pow_cycle(inputX, inputY))
print("With pow():", pow(inputX, inputY))
