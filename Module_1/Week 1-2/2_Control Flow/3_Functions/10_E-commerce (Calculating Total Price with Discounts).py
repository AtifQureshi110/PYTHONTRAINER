def calculate_total(cart, discount=0):
    """Calculates the total price of items in the cart, applying a discount."""
    total = sum(cart)
    final_price = total - (total * discount / 100)
    return final_price

# Real-world example:
cart_items = [100, 50, 30]  # Prices of items in the cart
discount_percentage = 10

print("Total Price:", calculate_total(cart_items, discount_percentage))  # Output: 162.0
