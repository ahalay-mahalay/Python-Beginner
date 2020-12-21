int_ = 10
float_ = 3.14
string_ = "text"
bool_ = False

print("int:", int_, "\nfloat: ", float_, "\nstring: " + string_, "\nbool:", bool_)

# ***********

name = input("What is your name? ")
age = int(input(f"Hello, {name}! How old are you? "))
if age >= 30:
    city = input(f"Oh, {name}! You are so... mature!\nWhere are you from? ")
else:
    city = input("Eh, youth...\nWhere are you from? ")

print(f"Glad to see you, {name} from {city}!\nHave a good day!")
