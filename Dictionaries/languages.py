favorite_languages = {
    "jen": "python",
    "sarah": "c#",
    "stef": "javascript",
    "edward": "ruby",
    "tycho": "javascript",
}

for name, language in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language is {language.title()}.")

print("\nThe people who took the poll are:")
for name in favorite_languages:  # Idem als favorite_languages.keys()
    print(name.title())

print()

friends = ["jen", "edward", "tycho"]
for name in favorite_languages:
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if "erin" not in favorite_languages:
    print("\nErin, please take our poll!")

for name in sorted(favorite_languages):
    print(f"{name.title()}, thank you for taking the poll!")

for language in set(
    favorite_languages.values()
):  # Genereert een set met unieke waarden
    print(language.title())

favorite_languages = {
    "jen": ["python", "ruby"],
    "sarah": ["c"],
    "edward": ["ruby", "go"],
    "phil": ["python", "haskell"],
}

for (
    name,
    languages,
) in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
