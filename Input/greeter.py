# name = input("Please enter your name: ")
# print(f"Hello, {name.title()}!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"Hello, {name.title()}!")

age = input("How old are you? ")
age = int(age)
if age >= 18:
    print(f"{name.title()}, you are old enough to vote!")
else:
    print(f"{name}, you are too young to vote.")
