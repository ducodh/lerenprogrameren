from fruitmand import fruitmand

langste_naam = ""
lengte_naam = 0
for x in fruitmand:
    naam = x.get("name")
    count = 0
    for x in naam:
        count += 1
        if count > lengte_naam:
            langste_naam = naam
            lengte_naam = count

for y in fruitmand:
    langste = y.get("name")
    if langste == langste_naam:
        kleur_EN = y.get("color")
        gewicht = y.get("weight")

X = "xxx"

print(f'de "{langste_naam}" ({lengte_naam} letters) heeft een {kleur_EN} kleur en een gewicht van {gewicht} kg.')