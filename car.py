'''A class that can be used to represent a car'''

class Car:
    '''A simple attempt to represent a Car'''
    def __init__(self, make, model, year):
        '''Atributes to describe the car'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        '''Return a neatly formatted descriptive name'''
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

    def read_odometer(self):
        '''Print a statement showing the car's mileage'''
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Don't try to roll it back Bitch!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles