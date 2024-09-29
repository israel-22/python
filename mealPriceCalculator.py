# For Santos Israel
# Meal Price Calculator
# This program calculates the total cost of a meal for children and adults, including sales tax, and provides the change from a given payment amount.

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
    cup_tax = float(input("\nWhat is the tax rate? (e.g., enter 6.5 for 6.5%) "))

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

    # Additional functionality: Calculate suggested tip (10%, 15%, 20%)
    print("\n--- Additional Information ---")
    tip_10 = total * 0.10
    tip_15 = total * 0.15
    tip_20 = total * 0.20
    print(f"Suggested Tips: \n10% = ${tip_10:.2f} \n15% = ${tip_15:.2f} \n20% = ${tip_20:.2f}")

    # Additional functionality: Discounts (if total exceeds a certain amount)
    if total > 100:
        discount = total * 0.10  # 10% discount
        discounted_total = total - discount
        print(f"\nCongratulations! You've received a 10% discount. Discounted Total: ${discounted_total:.2f}")
    else:
        print("\nSpend more than $100 to receive a 10% discount on your total!")

# Call the function
calculate_meal_price()
