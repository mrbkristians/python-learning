'''
Comparing
'''

car = "bmw"

# Checking for equality
car == "bmw" # True
car == "audi" # False
car.lower() == "bmw" # True

# Checking for inequality
if car != "audi":  # True
    print(f"Is not a {car.upper()}")
print("\n")


'''
Numerical Comparisons
'''

age = 18
age_0 = 25

age == 18 # True
age != 18 # False
age > 25 # False
age < 25 # True
age >= 18 # True
age <= 15 # False

# Check both conditions are both True 
(age == 18) and (age_0 > 23) # True
(age == 12) and (age_0 < 30) # False

# An OR expression fails only when both individual tests fail
(age == 18) or (age_0 > 30) # True
(age >= 20) or (age_0 <= 12) # False
