alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}

aliens = [alien_0, alien_1, alien_2]
print("\n")
for alien in aliens: 
    print(alien)
print("\n")

# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {"color": "yellow", "points": "3", "speed": "slow"}
    aliens.append(new_alien)
print("\n")

# Total amount of maden aliens

print(f"Total amount of aliens: {len(aliens)}")

print("\n")

# Change the values of the 3 first aliens in the list
for alien in aliens[:3]:
    if alien["color"] == "yellow":
        alien["color"] = "red"
        alien["points"] = 20
        alien["speed"] = "fast"

# Show first 5  aliens
for alien in aliens[:5]:
    print(alien)
print("\n")

'''
Nesting list in dictionary
'''

modify_aliens = {
    "color": "purple",
    "vepons": ["knife", "sword", "shield"],
    "speed": "medium"
}