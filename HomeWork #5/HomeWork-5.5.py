# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
while True:
    is_digit = True
    numbers = input("Enter digits separated by whitespaces: ")
    for i in numbers.split():
        if not i.isdigit():
            is_digit = False
            break
    if is_digit is True:
        break

with open("homework-5.5.txt", "w", encoding="utf-8") as file:
    file.write(numbers)

with open("homework-5.5.txt", "r", encoding="utf-8") as f:
    f_sum = 0
    for line in f:
        line = line.split()
        for i in line:
            f_sum += int(i)
print(f_sum)
