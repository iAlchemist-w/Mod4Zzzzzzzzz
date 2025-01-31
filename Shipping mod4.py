print("Hello, thank you for shopping with us.")

order_total = float(input("Enter the total order amount: $"))
if order_total < 50:
    shipping_cost = 5
    print(f"Shipping cost: ${shipping_cost}")
    shipping_cost = 0

total_cost = order_total + shipping_cost
print("The total cost, including shipping, is: $", total_cost)
