class Restaurant:
    '''Describe a restaurant'''
    def __init__(self, restaurant_name, cuisine_type,):
        '''Initialize restaurant name and cuisine type'''
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def set_number_served(self, customer):
        '''Add number of customers'''
        self.number_served += customer

class IceCreamStand(Restaurant):
    '''Describe a ice cream stand'''
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["chocolate", "vanilla", "strawberry"]

my_restaurant = Restaurant("taco hurt", "mexican")
my_restaurant.number_served = 43

print(f"\nMy Restaurant name is {my_restaurant.restaurant_name} and is {my_restaurant.cuisine_type} cuisine.")
print(f"\nLas hour served: {my_restaurant.number_served} people.")

my_restaurant.set_number_served(24)

print(f"\nToday served: {my_restaurant.number_served} people.")

ice_cream_shop = IceCreamStand("ice cum cream", "american")
print(ice_cream_shop.flavors)
