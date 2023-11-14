cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

age_0 = 22
age_1 = 17

print(age_0 >= 18 and age_1 >= 18)
print(age_0 >= 18 or age_1 >= 18)

requested_toppings = ["mushrooms", "onions", "pineapple", "cheese"]
print("mushrooms" not in requested_toppings)

age = 18

if age <= 12:
    price = 6
elif age <= 25 or age >= 60:
    price = 8.5
else:
    price = 9

print(f"The price of your ticket is € {price}\n")

requested_toppings = ["Cream", "Bacon"]

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping} to your pizza.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

available_toppings = (
    "mushrooms",
    "bacon",
    "olives",
    "green peppers",
    "pepperoni",
    "pineapple",
)
requested_toppings = [
    "mushrooms",
    "cheese",
    "olives",
    "green peppers",
    "bacon",
    "anchovies",
]

added_toppings = []
for topping in requested_toppings:
    if topping in available_toppings:
        print(f"Adding {topping} to your pizza.")
        added_toppings.append(topping)
    else:
        print(f"{topping} is not available as a topping (right now)")
toppings_on_pizza = ""
for topping in added_toppings:
    if topping != added_toppings[-1] and topping != added_toppings[-2]:
        toppings_on_pizza += f"{topping}, "
    elif topping == added_toppings[-2]:
        toppings_on_pizza += f"{topping} "
    else:
        toppings_on_pizza += f"and {topping}"
print(f"Finished making your pizza with {toppings_on_pizza}.")
