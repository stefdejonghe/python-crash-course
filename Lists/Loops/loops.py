magicians = ["alice", "timo", "david", "caroline"]
for value in range(1, 11):
    for magician in magicians:
        print(f"{magician.title()}, that was a great trick!")
        print(f"I can't wait to see your next trick, {magician.title()}")

print("Thank you everyone. That was a great magic show!")

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

# Bovenstaande kan ook als volgt geschreven worden:
squares = [value**2 for value in range(1, 11)]
print(squares)

digits = list(range(1, 10))
digits.append(0)
print(digits)

print(min(digits))
print(max(digits))
print(sum(digits))

players = ["Charles", "Steven", "Anton", "Pablo", "Jasza", "Tycho"]
print(players)
print(players[2:3])
print(players[:3])
print(players[2:])

print("Here are the first three players of the team")
for player in players[:3]:
    print(player)

my_foods = ["Pizza", "Fries", "Pasta Pesto"]
friends_foods = my_foods  # Dit legt een reference naar dezelfde lijst.

my_foods.append(
    "Cake"
)  # Aangezien beide variabelen verwijzen naar dezelfde lijst, wordt "Cake" ook toegevoegd aan friends_food.
print(friends_foods)

my_foods = ["Pizza", "Fries", "Pasta Pesto"]
friends_foods = my_foods[
    :
]  # Dit zorgt voor een nieuwe lijst met als resultaat een kopie van de oorspronkelijke lijst.

my_foods.append("Cake")
print(my_foods)
print(friends_foods)

# Onderstaande is een voorbeeld van 'Tuples'. Dit zijn lijsten die niet te veranderen zijn.
dimensions = (200, 50, 5)
for dimension in dimensions:
    print(dimension)
