def int_func(little_latin):
    titled_latin = ""
    for i in range(len(little_latin)):
        if (ord(little_latin[i]) in range(97, 123)) or (little_latin[i] == " "):
            if (i == 0) or (little_latin[i - 1] == " "):
                titled_latin += chr(ord(little_latin[i]) - 32)
            else:
                titled_latin += little_latin[i]
        else:
            print("You should have entered word(s) in small latin letters.")
            break
    return titled_latin


print(int_func(input("Enter your a word or words in small latin letters separated by whitespaces: ")))
