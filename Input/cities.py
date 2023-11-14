cities = []
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == "quit":
        print(
            "Thank you for taking our survey! You find a list of your visited cities here:"
        )
        for city in sorted(cities):
            print(f"\t{city}")
        break
    elif city == "del":
        del cities[-1]
    else:
        cities.append(city)
