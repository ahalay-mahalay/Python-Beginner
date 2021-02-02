# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.

# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить ее в словарь (со значением убытков).

# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import json

with open("homework-5.7.txt", "r", encoding="utf-8") as f:
    firm_dict = {}
    profitable_firms = 0
    firms_profit = 0
    for line in f:
        line = line.split()
        proceeds = int(line[2])
        costs = int(line[3])
        profit = proceeds - costs
        firm_dict[line[0]] = profit
        if profit >= 0:
            profitable_firms += 1
            firms_profit += profit
    average_profit = firms_profit / profitable_firms
    average_dict = {"Average_profit": average_profit}
    json_list = [firm_dict, average_dict]
    with open("homework-5.7.json", "w", encoding="utf-8") as j:
        print(json.dumps(json_list, indent=4, ensure_ascii=False), file=j)
