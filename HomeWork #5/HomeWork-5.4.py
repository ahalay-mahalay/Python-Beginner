# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
with open("homework-5.4-eng.txt", "r", encoding="utf-8") as eng:
    with open("homework-5.4-rus.txt", "w", encoding="utf-8") as rus:
        for line in eng:
            line = line.split()
            if line[2] == "1":
                line[0] = "Один"
                rus.write(f"{' '.join(line)}\n")
            if line[2] == "2":
                line[0] = "Два"
                rus.write(f"{' '.join(line)}\n")
            if line[2] == "3":
                line[0] = "Три"
                rus.write(f"{' '.join(line)}\n")
            if line[2] == "4":
                line[0] = "Четыре"
                rus.write(f"{' '.join(line)}\n")
