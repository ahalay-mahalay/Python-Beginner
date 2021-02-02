def division(dividend, divider):
    while divider == 0:
        divider = int(input("Divider cannot be Zero.\nEnter divider: "))
    return dividend / divider


print(division(int(input("Enter dividend: ")), int(input("Enter divider: "))))
