auto_merken = ("opel", "mercedes", "volkswagen","audi")
kleuren = ("rood", "geel", "blauw", "paars", "grijs")

brochure = []

for merk in auto_merken:
    for kleur in kleuren:
        auto_in_kleur = merk + " in " + kleur
        brochure.append(auto_in_kleur)

print(brochure)