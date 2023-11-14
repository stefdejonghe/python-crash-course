def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")


greet_user("Stef")


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:
    print("\nPlease tell me your name:")
    print("You can always type 'q' to quit.")
    f_name = input("First name: ")
    if f_name == "q":
        break
    l_name = input("Last name: ")
    if l_name == "q":
        break
    formatted_name = get_formatted_name(first_name=f_name, last_name=l_name)
    print(f"Hello, {formatted_name}!")


def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ["hannah", "tycho", "margot"]
greet_users(usernames)
