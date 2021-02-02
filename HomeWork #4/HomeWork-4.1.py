from sys import argv

name, production, rate, prize = argv
print(f"Employee salary is {(int(production) * int(rate)) + int(prize)}")
