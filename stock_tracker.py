import csv

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 185,
    "RELIANCE": 1300,
    "TCS": 4100
}

portfolio = {}
total_investment = 0

print("--- Welcome to Stock Portfolio Tracker ---")
print("Available Stocks & Prices:", ", ".join([f"{k} (${v})" for k, v in stock_prices.items()]))
print("Type 'done' when you finish adding stocks.\n")

# taking input from user stocks and their quantity
while True:
    stock_name = input("Enter stock symbol (e.g., AAPL, TSLA): ").strip().upper()
    
    if stock_name == "DONE":
        break
        
    if stock_name not in stock_prices:
        print(f"Error: '{stock_name}' is not in the available stock list. Please try again.\n")
        continue
        
    try:
        quantity = int(input(f"Enter quantity for {stock_name}: "))
        if quantity <= 0:
            print("Quantity must be greater than 0.\n")
            continue
    except ValueError:
        print("Invalid input! Please enter a valid whole number for quantity.\n")
        continue
        
    # add update quantity
    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
    print(f"Added {quantity} shares of {stock_name}.\n")

# calculate the total investment and display
print("\n--- Your Portfolio Summary ---")
if not portfolio:
    print("No stocks were added to your portfolio.")
else:
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = price * qty
        total_investment += value
        print(f"{stock}: {qty} shares x ${price} = ${value}")
        
    print(f"\nTotal Investment Value: ${total_investment}")

    # save the result in two format .txt and .csv
    save_choice = input("\nDo you want to save this summary to a file? (yes/no): ").strip().lower()
    if save_choice in ["yes", "y"]:
        file_format = input("Choose format - type 'txt' or 'csv': ").strip().lower()
        
        if file_format == "csv":
            with open("portfolio_summary.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Stock Symbol", "Quantity", "Price per Share ($)", "Total Value ($)"])
                for stock, qty in portfolio.items():
                    writer.writerow([stock, qty, stock_prices[stock], stock_prices[stock] * qty])
                writer.writerow(["TOTAL", "", "", total_investment])
            print("Saved successfully as 'portfolio_summary.csv'!")
            
        else:
            with open("portfolio_summary.txt", "w") as file:
                file.write("--- Stock Portfolio Summary ---\n")
                for stock, qty in portfolio.items():
                    file.write(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${stock_prices[stock] * qty}\n")
                file.write(f"\nTotal Investment Value: ${total_investment}\n")
            print("Saved successfully as 'portfolio_summary.txt'!")