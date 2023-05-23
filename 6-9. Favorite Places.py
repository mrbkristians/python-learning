
favorite_place = {
    "jen": ["New York"],
    "sarah": ["Los Angeles"],
    "edvard": ["Tokyo"],
    "phil": ["Seattle"],
    "sallia": ["San Francisco", "Los Angeles"],
}

for name, places in favorite_place.items(): # loops caur favorite_places
    if len(places) > 1:
        print(f"\n{name.title()} favorite places:")
        for place in places:
            print(f"\t{place.title()}")
    elif len(places) == 1:
        print(f"\n{name.title()} favorite place:")
        print(f"\t{places[0].title()}")

print("\n")
