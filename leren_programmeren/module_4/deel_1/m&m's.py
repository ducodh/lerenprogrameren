import random
tuple= ("oranje", "blauw", "groen", "bruin")
zak = []
hoeveel = int(input("hoeveel m&m's? "))
for i in range(hoeveel):
    kleur = random.randint(0,3)
    zak.append(tuple[kleur])
print (zak)