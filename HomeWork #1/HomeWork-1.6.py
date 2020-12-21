result = int(input("Enter your current result (integer): "))
goal = int(input("Enter your goal (integer): "))
days = 1

while result < goal:
    result *= 1.1
    days += 1
print(f"On the {days} day athlete will achieve a result of at least {goal} km.")
