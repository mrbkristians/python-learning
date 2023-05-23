sandwich_orders = ['roast beef', 'pastrami', 'hummus', 'club meat', 'pastrami', 'hummus', 'club meat', 'pastrami', 'hummus', 'club meat']
out_off_stock = "pastrami"
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    if sandwich == out_off_stock:
        print(f"Sorry, we are out of {sandwich} today.")
        continue
    print(f"At the moment making {sandwich.title()} sandwitch!")
    finished_sandwiches.append(sandwich)
print("\nSandwiches that are ready:")
for sandwich in finished_sandwiches:
    print(sandwich.title())

print("\n")