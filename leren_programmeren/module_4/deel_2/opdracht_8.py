from fruitmand import fruitmand

gewicht = int()

watermeloen = {
    'name' : 'watermeloen',
    'weight' : 1769,
    'color' : 'green',
    'round' : True
    }

for i in range(7):
    plus = fruitmand[i].get("weight")
    gewicht += plus

fruitmand.append(watermeloen)

print(f"totaal gewicht: {gewicht}")