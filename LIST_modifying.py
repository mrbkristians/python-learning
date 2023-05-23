motorcycles = ["honda", "yamaha", "suzuki"]

motorcycles[0] = "zinco" # changes value of the first element in the list
motorcycles.append("aprillia") # append adds an item to the end of the list
motorcycles.insert(3, "husquarna") # insert adds element any place at the list by specifying the index and value
del motorcycles[1] #del deleats element 

print(motorcycles)

popped_motorcycle = motorcycles.pop() # poops out the last element
print(f"Pooped motorcycle: {popped_motorcycle.title()}!")

too_expencive = "suzuki"
motorcycles.remove(too_expencive) # removes by the value
print(f"I sold my {too_expencive.title()}, it was a too expencive for me.") 

motorcycles.sort() # sorts the list in alphabetical order
print(motorcycles)

motorcycles.sort(reverse=True) # sorts the list in reverse alphabetical order
print(motorcycles)

print(sorted(motorcycles)) # sorted function maintain the original order of the list
print(motorcycles)
print(sorted(motorcycles, reverse=True)) # sorted and reverse

motorcycles.reverse() # reverses the order of the list

motorcycles.insert(0, "ižs")

print(f"\nList of motorcycles:\n\t{motorcycles}")

bike_count = len(motorcycles) # counts the number of elements in the list
print(f"\nI have {bike_count} bikes.\n")

print(motorcycles[-1].title()) # index of the last element in the list