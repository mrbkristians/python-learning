def make_sandwitch(*toppings):
    print("\nOrdered sandwitch with the following toppings:")
    for topping in toppings:
        print(f"\t- {topping}")

make_sandwitch("pepperoni")
make_sandwitch("mushrooms", "green peppers", "extra cheese")
make_sandwitch("pepperoni", "mushrooms", "green peppers", "extra cheese")