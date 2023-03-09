import random

name = input("wat is je naam? ")
nr = int(input("voer een nummer in: "))

for c in range(nr):
    compliment = random.randint(1,4)
    if compliment == 1:
        print(f"je ziet er goed uit {name}!!!")
    elif compliment == 2:
        print(f"je bent geweldig {name}!!")
    elif compliment == 3:
        print (f"wow, {name}!")
    else:
        print(f"lekker gewerkt {name}")