rating = [7, 5, 3, 3, 2]
while True:
    number = int(input("Enter a natural number: "))

    for i in range(len(rating)):
        if (i == 0) and (number > rating[i]):
            rating.insert(i, number)
            break
        elif (i == len(rating) - 1) and (number <= rating[i]):
            rating.append(number)
            break
        elif (rating[i - 1] >= rating[i]) and (number > rating[i]):
            rating.insert(i, number)
            break
    print(rating)
