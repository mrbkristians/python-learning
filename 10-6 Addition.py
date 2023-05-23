
def addition():
    while True:
        print("Give me two numbers, and I'll sum them.")
        print("Enter 'q' to quit.")
        a = input("First number: ")
        if a == "q":
            break
        b = input("Second number: ")
        if b == "q":
            break
        try:
            answer = int(a) + int(b)
            print(f"Sum of number is: {answer}")
        except ValueError:
            print("Please enter numbers only!")

print("\n")
addition()



