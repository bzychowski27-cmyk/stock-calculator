# Version 2: Calculate Investment Profit and Return

shares = 10
share_price = 150
new_share_price = 175

investment_cost = shares * share_price
current_value = shares * new_share_price
profit = current_value - investment_cost
return_pct = (profit / investment_cost) * 100

print("STOCK INVESTMENT CALCULATOR")
print(f"Number of Shares: {shares}")
print(f"Purchase Price Per Share: ${share_price}")
print(f"Total Investment Cost: ${investment_cost}")
print(f"New Share Price: ${new_share_price}")
print(f"Current Investment Value: ${current_value}")
print(f"Profit: ${profit}")
print(f"Investment Return: {return_pct:.2f}%")
