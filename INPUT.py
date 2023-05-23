
print("\n")

# Simple INPUT example input()
message = input("Tell me something, and I will repeat it back to you: ")
print(f"\n{message.title()}")


#Several line prompt
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "What is your first name? " #  Set multiple prompt lines
name = input(prompt) 
print(f"\nHello, {name}!")


# Using int() to Accept Numerical Input
age =  input("\nHow old are you? ")
age = int(age)

''' Height checking example '''
height = input("How tall are you, in inches?")
height = int(height)
if height >= 48:
    print("Your tall anough to ride with us!")
else:
    missing = 48 - height
    print(f"You missing {missing} inches to ride BRO! ")

''' EVEN or ODD '''
number = input("Enter a number, and I'ļl tell you if itš even or odd: ")
number = int(number)
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nNumber {number} is odd.")


print("\n") #break in end