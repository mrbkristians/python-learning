class Car:
    '''Simple attempt to represent a car.'''

    def __init__(self,make, model, year):
        '''Initialize attributes to describe a car'''
        self.make = make # Attribute's
        self.model = model
        self.year = year
        self.odometer_reading = 0 # Attribute with initial Value 0

    def get_descriptive_name(self): # Methods
        '''Return a neatly formatted descriptive name.'''
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        '''Print a milage statement'''
        print(f"This car have: {self.odometer_reading} miles")

    def update_odometer(self, mileage): #Modifying Atribute's True the Funkcion
        '''Set the odometer reading to the given value'''
        '''Reject the try to roll mileage back'''
        if mileage >= self.odometer_reading: # makes a secnce before modifying attribute
            self.odometer_reading = mileage
        else: 
            print("Don't try to roll back mdfuck!")
    
    def increment_odometer(self, miles): # takes in a number of miles and adds this valuo to odometer_reading  
        '''Add the given amount to the odometer reading'''
        self.odometer_reading += miles




    
new_car = Car("mercedes", "clk 230", "1997")

print(new_car.get_descriptive_name())
new_car.read_odometer()

new_car.odometer_reading = 23 # Modifying an Attribute's Value Directly
new_car.read_odometer()

new_car.update_odometer(200) # calling  funktion with 200 as an argument (coresponding to the mileage parameter in the method definition)
new_car.read_odometer()

new_car.update_odometer(100) # When you try to go agains the logic

new_car.increment_odometer(400)
new_car.read_odometer()

