"""Pylint learnings for make better codes. Do not post, is book code."""
import sys
import random

print("Welcome to the Random Silly Name Generator. '\n")
print("Silly name:\n\n")

first = ('Smalls', 'Potato', 'Pookie', 'Grease')
middle = ('Dimmpy', 'Whipple', 'Fudruckers', 'TgiFridagnbees')
last = ('Wells', 'Michigan', 'Morton', 'Spongebob')

while True:
    first_name = random.choice(first)
    middle_name = random.choice(middle)
    last_name = random.choice(last)
    print("\n\n")
    print("{} {} {}".format(first_name, middle_name, last_name), file=sys.stderr)
    print("\n\n")
    try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")
    if try_again.lower() == "n":
        break
input("\nPress Enter to exit.")
