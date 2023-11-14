bicycles = ["Trek", "Cannondale", "Redline", "Specialized"]
print(bicycles)
print(bicycles[0])
print(bicycles[0].upper())
print(bicycles[-1])  # Returns last element in the list
print(bicycles[-3])  # Returns third last element in the list

message = f"My first bicycle was a {bicycles[0]}."

motorcycles = ["Honda", "Suzuki", "Ducati", "Yamaha"]
print(motorcycles)
motorcycles[2] = "Kawasaki"
print(motorcycles)
motorcycles.append("Ducati")
print(motorcycles)

motorcycles.insert(2, "BMW")
print(motorcycles)

del motorcycles[2]
print(motorcycles)
popped_motorcycle = motorcycles.pop(1)
print(f"{popped_motorcycle} was removed from the list")
print(motorcycles)

too_expensive = "Ducati"
index = motorcycles.index(too_expensive)
print(
    f"{motorcycles.pop(index)} was too expensive for me. That's why it is removed from the list."
)
print(motorcycles)

cars = [
    "Toyota",
    "BMW",
    "Mazda",
    "Opel",
    "Peugeot",
    "Nissan",
    "Alfa Romeo",
    "Audi",
    "Mercedes",
]
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

cars = [
    "Toyota",
    "BMW",
    "Mazda",
    "Opel",
    "Peugeot",
    "Nissan",
    "Alfa Romeo",
    "Audi",
    "Mercedes",
]

print(
    f"Here is the list temporarily sorted reverse alphabetically: {sorted(cars, reverse=True)}"
)
print(f"Here is the original list: {cars}")

print(f"There are {len(cars)} car brands in this list")

cars.reverse()
print(cars)
