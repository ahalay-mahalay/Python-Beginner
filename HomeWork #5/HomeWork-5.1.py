# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
with open("homework-5.1.txt", "w", encoding="utf-8") as f:
    data = input("Enter data. Empty string - exit: ")
    while data != "":
        f.write(f"{data}\n")
        data = input("Enter data. Empty string - exit: ")
