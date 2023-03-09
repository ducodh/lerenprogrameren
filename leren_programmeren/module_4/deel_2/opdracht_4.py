from fruitmand import fruitmand
import random

aantal=int(input("hoeveel stuks fruit? "))

for i in range(aantal):
    keuze = random.randint(0,6)
    naam = fruitmand[keuze].get('name')
    print(naam)