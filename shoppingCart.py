# Santos Israel - Shopping Cart Program

from datetime import datetime

def show_intro():
    print("***************************************************")
    print("**    Welcome to ABC Virtual Supermarket!        **")
    print("**  Here you can add, view, and remove items from **")
    print("**    your cart while managing your purchase.    **")
    print("** Enjoy a fast and easy shopping experience!     **")
    print("***************************************************\n")

def show_menu():
    print("\nPlease select one of the following options:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Calculate total")
    print("5. Apply discount (if total exceeds $100)")
    print("6. Empty cart")
    print("7. Exit")

def add_item(names, prices):
    name = input("What item would you like to add? ")
    price = float(input(f"What is the price of '{name}'? "))
    names.append(name)
    prices.append(price)
    print(f"'{name}' has been added to the cart.")

def view_cart(names, prices):
    if not names:
        print("The shopping cart is empty.")
        return
    print("The contents of the shopping cart are:")
    for i in range(len(names)):
        print(f"{i + 1}. {names[i]} - ${prices[i]:.2f}")

def remove_item(names, prices):
    view_cart(names, prices)
    if not names:
        return
    try:
        number = int(input("Which item would you like to remove? "))
        if 1 <= number <= len(names):
            removed_name = names.pop(number - 1)
            removed_price = prices.pop(number - 1)
            print(f"Item '{removed_name}' removed.")
        else:
            print("Sorry, that item number is not valid.")
    except ValueError:
        print("Please enter a valid number.")

def calculate_total(prices):
    total = sum(prices)
    print(f"The total price of the items in the shopping cart is: ${total:.2f}")
    return total

def apply_discount(prices):
    total = sum(prices)
    if total > 100:
        discount = total * 0.10
        total_with_discount = total - discount
        print(f"Congratulations! A 10% discount has been applied.")
        print(f"Original total: ${total:.2f}")
        print(f"Total after discount: ${total_with_discount:.2f}")
    else:
        print("Discounts apply only for totals over $100.")

def empty_cart(names, prices):
    confirmation = input("Are you sure you want to empty the cart? (yes/no): ").lower()
    if confirmation == 'yes':
        names.clear()
        prices.clear()
        print("The cart has been emptied.")
    else:
        print("The cart has not been emptied.")

def log_purchase():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Purchase logged on: {current_date}")

def main():
    names = []
    prices = []
    
    show_intro()
    
    while True:
        show_menu()
        option = input("Please enter an action: ")
        
        if option == '1':
            add_item(names, prices)
        elif option == '2':
            view_cart(names, prices)
        elif option == '3':
            remove_item(names, prices)
        elif option == '4':
            calculate_total(prices)
            log_purchase()  # Log the time of the purchase
        elif option == '5':
            apply_discount(prices)
        elif option == '6':
            empty_cart(names, prices)
        elif option == '7':
            print("Thank you. Goodbye.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
