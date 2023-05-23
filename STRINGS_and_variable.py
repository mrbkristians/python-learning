first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"\n \tHello, {full_name.title()}!\n"

print(message)

first_name_1 = "eric"
answer = input("yes/no")
message_2 = f"\n\tHello, {first_name_1.title()}!\n Would you like to learn the Python today?\n {answer}: \n"

if answer == "yes":
    print("Let's learn Python!")
else:
    print("\n\tGoodbye!")