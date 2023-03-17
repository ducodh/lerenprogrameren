from fruitmand import fruitmand

for x in fruitmand:
    naam = x.get("name")
    if naam == "appel":
        print(x.get("weight"))