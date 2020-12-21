number = 0
max_digit = 0
divider = 10
remainder = 1
while number <= 0:
    number = int(input("Enter a positive integer: "))

while remainder != 0:
    remainder = (number % divider) // (divider // 10)
    if max_digit < remainder:
        max_digit = remainder
    divider *= 10
print(f"Max digit is {max_digit}")
