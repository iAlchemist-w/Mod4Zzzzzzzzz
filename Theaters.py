print("Hello, and welcome to Galaxy Theaters. Please get ready to face our entry process.")

age = int(input("Please enter your age: "))

if age < 13:
    print("Hello, you can only watch rated G movies. You'll get the kids price at the concession stand!")
elif 13 <= age <= 17:
    print("Hi, you can watch PG-13 movies! Come by the concession stand for some refreshments!")
else:
    print("You can watch rated R movies! Want some popcorn to go with that?")
# Write your code here :-)
