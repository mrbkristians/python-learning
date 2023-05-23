print("\n")

responses = {}

polling_active = True # Set a flag to indicate that polling is active

while polling_active:
    name = input("\nWhat is your name? ")  # prompt for the person's name and response.
    response = input("Which mountain would you like to climd today?")

    responses[name] = response # Store the response in the dictionary.

    repeat = input("Would you like to let another person respond? (yes/no) ") # Find out if anoyone else is going to take the poll.
    if repeat == "no":
        polling_active = False

print("\n--- Poll Result ---") # Polling is complete. Show the result.
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response}.")


print("\n")