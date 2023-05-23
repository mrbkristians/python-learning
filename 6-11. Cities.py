cities = {
    "riga": {
        "country": "latvia",
        "population": 230000,
        "fact": "Half of population is russians"
        },
    "santa-cruz": {
        "country": "spain",
        "population": 1000000,
        "fact": "Canarians are fucking lazy"
        },
    "london": {
        "country": "england",
        "population": 222200000,
        "fact": "London is one of oldest cities",
        },
    }

print("\n")

for city, city_info in cities.items():
    print(f"\n\t\t\tCity: {city.title()}")
    print("\t\tSome information about it:")
    country = city_info["country"].title()
    population = city_info["population"]        
    fact = city_info["fact"]
    print(f"\t\tIt is located in {country}.")
    print(f"\t\tPopulation: {population}")
    print(f"\t Some interesting fact about the {city.title()}:\n\t{fact}.")
print("\n")