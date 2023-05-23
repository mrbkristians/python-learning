
aviable_toppings = ["mushrooms", "olives", "green peppers", "pepperoni", "pineapple", "extra cheese",  "beef", "chicken"]
request_toppings = ["mushrooms", "extra cheese", "french fries", "green peppers"]
finished_product = "green peppers"

if request_toppings: # Check if te list is with or without elements
    for requested_topping in request_toppings: # for loop true a list elements
        if requested_topping == finished_product: # if statement with special conditions for the items in the list
            print(f"\n\tSorry no {finished_product} tonight")
        else:
            print(f"\nAdding requested topping: {requested_topping.title()}")
else: # if list is empty
    print("You sure wanna plain pizza?")
print(f"\nYou want pizza without {finished_product}?\n")

print("\nWe put your order together:")
if request_toppings: 
    for request_topping in request_toppings:
        if request_topping in aviable_toppings: # check element from list 1 in the list 2
            print(f"\tAdding {request_topping.title()}")
        else:
            print(f"Sorry, No {request_topping.title()} tonight!")
print("Your pizza is Ready!\n")

