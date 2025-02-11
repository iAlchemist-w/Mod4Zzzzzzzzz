# Write your code here :-)
#1. Construct a truth table for the expression: (A AND B) OR (NOT B) where A and B each can be True or False. Your truth table should be commented out (as it's not valid Python code!)

# Write your code here :-)
#Truth table
#Boolean Values
# True | 0 | Off | No
# False| 1 | On | Yes
# It is not snowing outside (yet™)
# ™ = there is an infinite possibility that it might snow within the next few weeks given the cold temperatures

is_snowing = True #was true last week, it snowed on Monday, Wednesday, Thursday, Friday.
is_sunny = False #was true on Monday, Wednesday, Thursday, Friday
print(is_snowing) # Output: True
print(is_sunny) # Output: False
print(type(is_sunny))
print(type(is_snowing)) # Write your code here :-)
print("Hello, thank you for shopping with us.")



#2. The headlights of a car should only automatically turn on when the daylight outside is below a certain threshold. If a sensor threshold is below the number 8, print "Headlights On"; otherwise, print "Headlights Off".

# Write your code here :-)
sensor_threshold = 7
if not (sensor_threshold) >= 8:
    print("Headlights On! It's dark out!")
else:
    print("Headlights off, it is not dark out yet.")
#3. Prompt the user for their bank balance. Evaluate whether the balance is less than $100. Print True if the user’s balance is below $100; print False, otherwise.

# Write your code here :-)
print ("Welcome to our Bank!")
balance = float(input("Enter your bank balance: $"))
if balance < 100:
    print(True)
else:
    print(False)

#4
print("Hello, and welcome to Galaxy Theaters. Please get ready to face our entry process.")

age = int(input("Please enter your age: "))

if age < 13:
    print("Hello, you can only watch rated G movies. You'll get the kids price at the concession stand!")
elif 13 <= age <= 17:
    print("Hi, you can watch PG-13 movies! Come by the concession stand for some refreshments!")
else:
    print("You can watch rated R movies! Want some popcorn to go with that?")
#5 order total
order_total = float(input("Enter the total order amount: $"))
if order_total < 50:
    shipping_cost = 5
    print(f"Shipping cost: ${shipping_cost}")
    shipping_cost = 0

total_cost = order_total + shipping_cost
print("The total cost, including shipping, is: $", total_cost)
