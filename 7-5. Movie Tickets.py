
prompt = "\nHow old are you? "
prompt += "\nEnter your age: "
age = input(prompt)
age = int(age)

ticket = 0

if age < 3:
    ticket = 0
elif age > 12:
    ticket = 15
else:
    ticket = 10

print(f"\nYour ticket price is ${ticket}.")
print("\n")