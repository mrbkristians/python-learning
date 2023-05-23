print("\n")

#Return a simple Value
def get_formatted_name(first_name, last_name): # The definition of get_formatted_name() takes as parameters a first and last name
    '''Return a full name,neatly formatted.'''
    full_name = f"{first_name} {last_name}" # function assign result of combining first and last names and adding space between
    return full_name.title() # value of full_name is converted to tile case and returned
musician = get_formatted_name("jimi","hendrix") # when call a function that returns a value, need to provide a variable that the return value can be assigned to
print(f"\nTonight Live on stage {musician}!")

# RETURN DICTIONARY
# add new optional parameter age to the function definition and assign the parameter
def build_person(first_name, last_name, age=None): # None is when variable has no specific value assigned to it
    '''Return a dictionary od information'''
    person = {"first": first_name, "last": last_name }
    if age:
        person["age"] = age
    return person
musician = build_person("jimi", "hendrix")
print(musician)


