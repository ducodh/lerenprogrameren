import random
kleuren=("rood", "blauw", "groen", "geel", "bruin")
hoeveel = int(input("hoeveel m&m's? "))
 
bagOfMnMs = {}
for i in range(hoeveel):
    kleur = random.choice(kleuren)
    if kleur not in bagOfMnMs:
        bagOfMnMs.update({kleur: 1})
    
    elif kleur in bagOfMnMs:
        bagOfMnMs[kleur] +=1

print(bagOfMnMs)