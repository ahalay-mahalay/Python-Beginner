number = int(input("Enter the number of seconds: "))
hours = number // 3600
seconds = number % 60
minutes = (number % 3600 - seconds) // 60

print(f"{hours:02}:{minutes:02}:{seconds:02}")

# #     or this way
# seconds = int(input("Enter the number of seconds: "))
# print(f"{seconds // 3600:02}:{(seconds % 3600 - seconds % 60) // 60:02}:{seconds % 60:02}")
