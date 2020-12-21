proceeds = int(input("Enter proceeds: "))
costs = int(input("Enter costs: "))
profit = proceeds - costs
profitability = proceeds / costs

if profit > 0:
    print(f"Your profit is: {profit}")
    print(f"Your profitability is: {profitability:.2f}")
    employees = int(input("Enter the number of employees: "))
    print(f"Profit per employee is: {profit / employees:.2f}")
else:
    print(f"Your loss is: {profit}")
