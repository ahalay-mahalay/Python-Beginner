goods = []
n = 1
while True:
    print("Enter\033[1m QUIT\033[0;0m if you have finished entering data.")
    my_good = input("Enter name, price, count of your good separated by whitespaces: ")
    if my_good.lower() == "quit":
        break
    my_good = my_good.split(" ")
    my_dict = {"name": my_good[0], "price": int(my_good[1]), "count": int(my_good[2]), "unit": "piece"}
    my_tuple = (n, my_dict)
    n += 1
    goods.append(my_tuple)

my_names = []
my_prices = []
my_counts = []
my_units = []
for i in range(len(goods)):
    for j in range(len(goods[i])):
        my_names.append(goods[i][1]["name"])
        my_prices.append(goods[i][1]["price"])
        my_counts.append(goods[i][1]["count"])
        my_units.append(goods[i][1]["unit"])
        break
statistics = {"name": my_names, "price": my_prices, "count": my_counts, "unit": list(set(my_units))}
print(f"Goods: {goods}\nStatistics: {statistics}")
