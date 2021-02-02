number = 0
seasons_list = ['', 'winter', 'winter',
                'spring', 'spring', 'spring',
                'summer', 'summer', 'summer',
                'fall', 'fall', 'fall', 'winter']
seasons_dict = {'winter': [12, 1, 2],
                'spring': [3, 4, 5],
                'summer': [6, 7, 8],
                'fall': [9, 10, 11]}

while number not in range(1, 13):
    try:
        number = int(input("Enter the month number from 1 to 12: "))
    finally:
        continue
# list
print(f"It is {seasons_list[number]}")
# dictionary
for key, value in seasons_dict.items():
    if number in value:
        print(f"It is {key}")
        break
