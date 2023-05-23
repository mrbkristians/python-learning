def full_name_formatting(first_name, last_name):
    '''Return the full name'''
    full_name = f"{first_name} {last_name}"
    return full_name.title()
#  loop
print("\nPlease tell me your name")
print("(enter 'q' to quit)")
while True:
    print("\nPlease tell me your name")
    print("(enter 'q' to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = full_name_formatting(f_name, l_name)
    print(f"\n\t\tHello, {formatted_name}!")

