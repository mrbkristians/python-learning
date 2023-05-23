
pizza_toppings = []
prompt = "\nEnter the topping you want: "
prompt += "\nIf you finished with order type 'quit'! "

while True:
    new_toping = input(prompt)
    if new_toping == 'quit':
        break
    else:
        print(f"\nYou just added: {new_toping.title()}")
    pizza_toppings.append(new_toping)

print("\nYou just made a pizza with:")
for topping in pizza_toppings:
    print(topping.title())


print("\n")