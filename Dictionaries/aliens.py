alien_0 = {"color": "green", "points": 5}

print(alien_0["color"])
print(alien_0["points"])
print(alien_0)

alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

alien_0 = {}
print(alien_0)

alien_0["color"] = "green"
alien_0["points"] = 5
print(alien_0)

alien_0["x_position"] = 0
alien_0["y_position"] = 25
alien_0["speed"] = "medium"
print(
    f"Current position of the alien is x: {alien_0['x_position']} and y: {alien_0['y_position']}"
)

# Move the alien to the right
# Determine how far to move the alien based on its current speed
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3

alien_0["x_position"] += x_increment
print(
    f"Current position of the alien is x: {alien_0['x_position']} and y: {alien_0['y_position']}"
)

del alien_0["points"]
print(alien_0)

alien_0 = {"color": "green", "speed": "slow"}
# De get() methode zorgt ervoor dat er een standaard return kan geformuleerd worden, indien deze key niet bestaat.
# Dit zorgt voor minder errors
point_value = alien_0.get("points", "No point value assigned")
print(point_value)

# Een lijst van dictionaries
print("\nEen lijst van dictionaries:")
alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

aliens = []

for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")
