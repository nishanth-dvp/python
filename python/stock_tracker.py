stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 170,
    "MSFT": 420,
    "AMZN": 190
}

total_investment = 0
investment_details = []

print("===== Stock Tracker =====")
print("Available stocks:", ", ".join(stocks.keys()))

while True:
    stock = input("\nEnter stock name or 'done' to finish: ").upper()

    if stock == "DONE":
        break

    if stock not in stocks:
        print("Stock not available.")
        continue

    quantity = int(input("Enter quantity: "))

    value = stocks[stock] * quantity
    total_investment += value

    investment_details.append(
        [stock, stocks[stock], quantity, value]
    )

    print("Investment:", value)

print("\n===== Investment Summary =====")

for details in investment_details:
    print("Stock:", details[0])
    print("Price:", details[1])
    print("Quantity:", details[2])
    print("Investment:", details[3])
    print()

print("Total Investment:", total_investment)

save = input("Do you want to save the result? (yes/no): ").lower()

if save == "yes":
    with open("stock_investment.txt", "w") as file:
        file.write("===== Stock Investment Summary =====\n\n")

        for details in investment_details:
            file.write("Stock: " + details[0] + "\n")
            file.write("Price: " + str(details[1]) + "\n")
            file.write("Quantity: " + str(details[2]) + "\n")
            file.write("Investment: " + str(details[3]) + "\n")
            file.write("-----------------------------\n")

        file.write("\nTotal Investment: " + str(total_investment))

    print("Result saved to stock_investment.txt")

else:
    print("Thank you!")