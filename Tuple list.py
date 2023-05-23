# List that is possible to modify and change the elements
my_cars = ["bmw", "audi", "toyota", "subaru"]
print(my_cars)
my_cars.append("honda")
print(my_cars)


# TUPLE. LIst of tuples
# List where you can't modify the elements
dimensions = (20, 50) # define a tuple

print(dimensions[0])
print(dimensions[1])

my_t = (3,) # define a tuple with a single element, always leave a comma to a element.

# Looping through all values in a tuple
for dimension in dimensions:
    print(f"\t{dimension}\n")

dimensions = (400, 100) #  Although can't modify tuple list but is possible reassigne it with new values

print(f"\n")
for dimension in dimensions:
    print(f"\t{dimension}")
print(f"\n")

'''
Use the tuple  when you store some data that sould not be chanched
'''

