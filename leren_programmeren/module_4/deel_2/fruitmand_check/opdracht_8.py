from fruitmand import fruitmand

gewicht = 0

watermeloen = {
    'name' : 'watermeloen',
    'weight' : 1769,
    'color' : 'green',
    'round' : True
    }

for i in fruitmand:
    plus = i.get("weight")
    gewicht += plus

fruitmand.append(watermeloen)

print(f"totaal gewicht: {gewicht}")