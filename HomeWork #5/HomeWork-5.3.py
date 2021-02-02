# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
with open("homework-5.3.txt", "r", encoding="utf-8") as f:
    count = 0
    total_income = 0
    print("Salary less than 20000:")
    for line in f:
        count += 1
        line = line.split()
        if float(line[1]) < 20000:
            print(line[0])
        total_income += float(line[1])
    print(f"Average income: {total_income / count}")
