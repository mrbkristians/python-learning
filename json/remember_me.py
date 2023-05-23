import json

def greet_user():
    filename = "/Users/djkistians/Documents/GitHub/PYTHON-LEARNING/json/username.json"
    try:
        with open(filename) as f:
            username = json.load(f) 
    except FileNotFoundError:
        username = input("Enter your username: ")
        with open(filename, "w") as f:
            json.dump(username, f)
            print(f"We'll remember you when see you again, {username}!")
    else:
        print(f"Welcome back, {username}!")

greet_user()
