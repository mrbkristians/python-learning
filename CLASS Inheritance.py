class Car:
    '''A simple attempt to present a car'''

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def incremet_odometer(self, miles):
        self.odometer_reading += miles
    
    def fill_gas_tank(self):
        print("You have to fill up the tank")


class Battery:
    '''Model battery'''
    def __init__(self, battery_size=75):
        '''Initialize the battery attribute'''
        self.battery_size = battery_size

    def describe_battery(self):
        '''Print a statement describing the battery size'''
        print(f"This car has a {self.battery_size}--kWh battery.")
    
    def get_range(self):
        '''Print a statement about the range of this battery'''
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on full charge.")


'''The __init__() Method for a Child Class'''
class ElectricCar(Car): # define the child class. The name of the parent class must be included in parenties in the definiton of a child class
    '''
    Represent aspects of a car, specific to electric vehiles
    Initialize attributes of the parent class
    '''
    def __init__(self, make, model, year):
        super().__init__(make, model, year) # super() function allows call a method from parent class
        self.battery = Battery()
     
    def fill_gas_tank(self):
        print("This car is Fully Electric You Prick!")
    


my_tesla = ElectricCar("tesla", "model", 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()