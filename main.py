# Hardcoded stock prices dictionary
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 310
}

def print_portfolio(portfolio):
    if not portfolio:
        print("📭 Portfolio is currently empty.")
        return
    print("\n🧾 Current Portfolio Summary:")
    total_value = 0
    for stock, qty in portfolio.items():
        value = stock_prices[stock] * qty
        print(f"{stock} - {qty} shares @ ${stock_prices[stock]} = ${value}")
        total_value += value
    print(f"\n💰 Total Investment Value: ${total_value}")
    return total_value

def stock_portfolio_tracker():
    print("📈 Welcome to the Stock Portfolio Tracker")
    print("Available stocks:", ", ".join(stock_prices.keys()))
    print("Commands: 'done' to finish, 'view' to see current portfolio, 'remove' to delete a stock, 'edit' to change quantity\n")

    portfolio = {}

    while True:
        stock = input("Enter stock symbol or command: ").strip().upper()

        if stock == "DONE":
            break
        
        elif stock == "VIEW":
            print_portfolio(portfolio)
            continue
        
        elif stock == "REMOVE":
            if not portfolio:
                print("📭 Portfolio is empty, nothing to remove.")
                continue
            rem_stock = input("Enter stock symbol to remove: ").strip().upper()
            if rem_stock in portfolio:
                del portfolio[rem_stock]
                print(f"🗑 Removed {rem_stock} from portfolio.")
            else:
                print("⚠ Stock not found in portfolio.")
            continue
        
        elif stock == "EDIT":
            if not portfolio:
                print("📭 Portfolio is empty, nothing to edit.")
                continue
            edit_stock = input("Enter stock symbol to edit: ").strip().upper()
            if edit_stock in portfolio:
                try:
                    new_qty = int(input(f"Enter new quantity for {edit_stock}: "))
                    if new_qty <= 0:
                        del portfolio[edit_stock]
                        print(f"🗑 Quantity zero or less, removed {edit_stock} from portfolio.")
                    else:
                        portfolio[edit_stock] = new_qty
                        print(f"✏ Updated {edit_stock} quantity to {new_qty}.")
                except ValueError:
                    print("⚠ Invalid number entered.")
            else:
                print("⚠ Stock not found in portfolio.")
            continue
        
        else:
            if stock not in stock_prices:
                print("⚠ Stock not found. Please enter a valid stock symbol or command.")
                continue
            try:
                quantity = int(input(f"Enter quantity of {stock}: "))
                if quantity <= 0:
                    print("⚠ Quantity must be a positive integer.")
                    continue
            except ValueError:
                print("⚠ Please enter a valid number.")
                continue
            
            portfolio[stock] = portfolio.get(stock, 0) + quantity
            print(f"✅ Added {quantity} shares of {stock}.")

    # After exiting input loop, print final summary
    total_value = print_portfolio(portfolio)

    # Save option
    if portfolio:
        save = input("\nDo you want to save this result to a file? (yes/no): ").strip().lower()
        if save == "yes":
            filename = "portfolio_summary.txt"
            with open(filename, "w") as file:
                file.write("📈 Portfolio Summary:\n")
                for stock, qty in portfolio.items():
                    file.write(f"{stock} - {qty} shares @ ${stock_prices[stock]} = ${stock_prices[stock] * qty}\n")
                file.write(f"\n💰 Total Investment Value: ${total_value}\n")
            print(f"📂 Summary saved to {filename}")
    else:
        print("📭 No stocks in portfolio to save.")

# Run the enhanced program
stock_portfolio_tracker()