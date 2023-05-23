
sukabook = {
    "person_1": {
        "first_name": "anna", 
        "last_name": "abola", 
        "age": "21", 
        "city": "riga",
        },
    "person_2": {
        "first_name": "jana", 
        "last_name": "rezina", 
        "age": "45", 
        "city": "jelgava",
        },
    "person_3": {
        "first_name": "lara", 
        "last_name": "karpa", 
        "age": "23", 
        "city": "ventspils",},
    "person_4": {
        "first_name": "aksels", 
        "last_name": "berzs", 
        "age": "12", 
        "city": "costa adeje",
        },
    "person_5": {
        "first_name": "vaksels",
        "last_name": "paksels", 
        "age": "2", 
        "city": "tev piss",
        },
}

favorite_numbers = {
    "person_0": [1, 3], 
    "person_1": [2, 4],
    "person_2": [3],
    "person_3": [4],
    "person_4": [5, 4, 7],
    "person_5": [6],
    }

print("\n")

for users, user_info in sukabook.items():
    full_name = f"{user_info['first_name'].title()} {user_info['last_name'].title()}"
    age = user_info["age"]
    city = user_info["city"].title()
    print(f"\nUsername: {users.title()}")
    print(f"\tFull name: {full_name}")
    print(f"\tAge: {age}")
    print(f"\tCity: {city}")
    for user, numbers in favorite_numbers.items():
        if user == users:
            if len(numbers) > 1:
                print(f"\tFavorite numbers:")
                for number in numbers:     
                    print(f"\t\t{number}")
            elif len(numbers) == 1:
                print(f"\tFavorite number: {numbers[0]}")
print("\n")








