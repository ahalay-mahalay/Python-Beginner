# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
with open("homework-5.2.txt", "r", encoding="utf-8") as f:
    count = 0
    words = 0
    for line in f:
        words = line.split()
        count += 1
        s = "s"
        if len(words) == 1:
            s = ""
        print(f"In {count} line {len(words)} word{s}.")

print(f"Total lines in the file: {count}")
