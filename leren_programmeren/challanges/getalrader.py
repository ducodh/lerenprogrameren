import random

max_getal = 1000
min_getal = 0

input("bedenk een getal tussen de 0 en de 1000 en klik enter om te starten")

while True:
    quess = random.randint(min_getal,max_getal)
    hlg = input(f"{quess}, hlg: ")
    if hlg == "h":
        min_getal = quess
    elif hlg == "l":
        max_getal = quess 
    elif hlg == "g":
        print ("haha ik win")
        break
    else:
        break