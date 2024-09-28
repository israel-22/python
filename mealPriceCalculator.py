#For Santos Israel

def calculate_meal_price():
# Calculate meal price
    price_meal_children = float(input("How much does the meal cost for children? ")) 
    price_meal_adults = float(input("How much does the meal cost for adults? "))
    number_children = int(input("How many children are there? "))
    number_adults = int(input("How many adults are there? "))

    # Calculate subtotal price
    subtotal_price = (price_meal_children * number_children) + (price_meal_adults * number_adults)
    print(f"\nSubtotal price: ${subtotal_price:.2f}")

    # Calculate tax rate
    cup_tax = float(input("\nWhat is the tax rate? "))


    # Calculate sales tax
    sales_tax = subtotal_price * (cup_tax / 100)
    print(f"Sales tax: ${sales_tax:.2f}")

    # Calculate total
    total = subtotal_price + sales_tax
    print(f"Total: ${total:.2f}")

    # Request payment amount
    payment_amount = float(input("\nWhat is the payment amount? "))

    # Calculate change
    change = payment_amount - total
    print(f"Change: ${change:.2f}")

# Call the function
calculate_meal_price()
