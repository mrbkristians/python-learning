
'''Creating the Class'''
class Dog: # Define a class
    '''Simple attempt to model a dog.''' # Write a docstring describing what class does
    def __init__(self, name, age):
        '''Initialize the name and attributes'''
        self.name = name
        self.age = age
    def sit(self):
        '''Simulate a dog sitting in response to a command'''
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        '''Simulate rolling over in response to a command'''
        print(f"{self.name} rolled over!")

my_dog = Dog("willie", 6) 
my_dog.sit()
my_dog.roll_over()

print(f"My dog's name is {my_dog.name.title()}.") # acess the attributes of an instance
print(f"My dog is {my_dog.age} years old.")