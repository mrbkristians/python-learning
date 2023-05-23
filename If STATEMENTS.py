'''
IF Statemants
'''

#Simple if statemetns

# if contitional_test:
#     do_something()

# if else statemetns
age = 17
print("\nAge checking to Vote!")
if age >= 18:
    print("\tYou are old enough to vote\n")
    print("Have you registrated to vote?\n")
else: 
    print("\tGo home little homie!\n")
    print("Please register to vote as you turn 18")



cars = ["audi", "maserati", "nissan", "toyota", "ferrari", "bmw", "lamborghini"]
print("\n")
print(f"Original List:\n\t{cars}\n")
print(f"Modifyed List:")
for car in cars: # make a for loop on a list of cars
    if car == "bmw": # make if statement to look for element in lis  "bmw" and print it uppecase
        
        print(f"\t{car.upper()}")
    else: # any other element print title case
        print(f"\t{car.title()}")
print("\n")

# If Elif else statemetns
age = 12
print("\n")
if age < 4:
    print(f"At age: {age}")
    print("\tYour boat trip ticket is 0$.\n")
elif age < 18:
    print(f"At age: {age}")
    print("\tYour boat trip ticket is $25.\n")
else:
    print(f"At age: {age}")
    print("\tYour boat trip ticket is $40\n")


# Set price in a if-elif-else chain

age = 14

if age < 4:
    price = 0 #set value in the if-elif chain
elif age < 18:
    price = 25
elif age < 65: # Multiple elif Block
    price = 40
elif age >= 65: # Ommit The else Block
    price = 20

print(f"\nAt age: {age}")
print(f"\tYour boat trip ticket price is ${price} !\n")

# Testing multiple Conditions
 
requested_topping = ["mushrooms", "extra cheese"]

print("\n")
print("Extra toppings:\n")
if "mushrooms" in requested_topping:
    print("\tAdding mushrooms")
if "pepperoni" in requested_topping:
    print("\tAdding pepperoni")
if "extra cheese" in requested_topping:
    print("\tAdding extra cheese")

print("\nFinished making your pizza!\n")