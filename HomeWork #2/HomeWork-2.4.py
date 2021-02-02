words = input("Enter words separated by whitespaces: ")
words = words.split(" ")

for i, word in enumerate(words, 1):
    print(i, word[:10])
