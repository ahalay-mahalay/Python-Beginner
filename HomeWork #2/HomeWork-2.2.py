my_list = input("Enter your list separated by whitespaces: ")
my_list = my_list.split(" ")
for i in range(len(my_list)):
    if (i == (len(my_list) - 1)) and (len(my_list) % 2 == 1):
        break
    if i % 2 == 0:
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
print(my_list)
