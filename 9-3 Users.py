class User:
    '''User in the system'''

    def __init__(self, first_name, last_name, age, gender):
        '''Made user'''
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.gender = gender
        self.login_attemps = 0

    def describe_user(self):
        '''Build user portfolio'''
        name = f"Users Name: {self.first_name}"
        surname = f"Users Surname: {self.last_name}"
        age = f"Users age: {self.age}"
        gender = f"User is a {self.gender}"
        print(name)
        print(surname)
        print(age)
        print(gender)
        
    def greet_user(self):
        '''Greet user'''
        greeting = f"Hello {self.first_name}"
        print(greeting)

    def increment_login_attemps(self):
        '''increse login atemps'''
        self.login_attemps += 1
        
    def reset_login_aattemps(self):
        '''reset login attemps'''
        self.login_attemps = 0

user_1 = User("arturs", "strazdz", 56, "female")

user_1.greet_user()
user_1.describe_user()
user_1.increment_login_attemps()
print(user_1.login_attemps)
user_1.increment_login_attemps()
print(f"Loggin attemps: {user_1.login_attemps}")
