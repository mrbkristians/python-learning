
numbers = list(range(1, 10)) # Make a list of numbers from 1 till 9

print(f"\n{numbers}\n")

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
        
print("\n")