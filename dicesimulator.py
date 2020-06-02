import random

min_val=1
max_val=6

again = True

while again:
    print(random.randint(min_val,max_val))

    next_roll = input("Do you want to roll dice again?")

    if next_roll == "yes" or next_roll == "y":
        again = True

    else:
        again = False
