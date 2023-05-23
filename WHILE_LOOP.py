# Loop counts till 5
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# Set FLAG to quite while loop
prompt = "\nTell me something, and will repeat it: " # nosaka prompt
prompt += "\nEnter quit to end the program. " # make propt in multiple lines
message = "" # empty string for input message
active = True # set variable active to True
while active:  # set program in active state. as long as the active is True program is running
    message = input(prompt)
    if message == "quit":
        active = False 
    else:
        print(message)

# Set the BRAKE to quit the loop
prompt = "\nTell me the city you been visiting: "
prompt += "\nEnter 'quit' to end the program. "
while True:
    city = input(prompt)
    if city == 'quit': # Set the BKARE condition
        break # break the loop
    else:
        print("PFFF")
        print(f"I'd been to {city.title()} already PFF!")

# Using continue in a Loop
current_number = 0 # first set the starting point
while current_number < 10: # if the start number is less the python enters the loop
    current_number += 1 # increment the count by 1
    if current_number %2 == 0: # If statem check modulo of current_number and 2
        continue # if current_number id divisible by 2 it continues
    print(current_number) # if not it prints it and then restarts