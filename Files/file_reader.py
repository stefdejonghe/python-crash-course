import os

print(os.getcwd())

filename = "pi_digits.txt"

with open(filename) as file_object:
    contents = file_object.read()
print(f"{contents}\n")

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
