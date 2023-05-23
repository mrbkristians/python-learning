
alien_color = ["green", "yellow", "red"] # List of alien colors
shooted_alien = [alien_color[0], alien_color[2]] # List of shooted aliens
points = [] # free araay for the count of points

for dead in shooted_alien:
    if "green" in shooted_alien:
        points.append(5)
    if "yellow" in shooted_alien:
        points.append(10)
    if "red" in shooted_alien:
        points.append(15)
    print(f"\n\tYou just shooted: {dead.title()} alien!")

sum_of_game = sum(points)
print(f"\n\tYou got {sum_of_game} points!")

