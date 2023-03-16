from fruitmand import fruitmand

colors={}
for x in fruitmand:
    colors.update({x.get("color"): x.get("name")})

teller_rond = 0
teller_niet_rond = 0
while True:   
    color_choise = input("name a color: ")
    if color_choise not in colors:
        print(f'the color {color_choise} is not in "fruitmand"')
    else:
        for i in fruitmand:
            if i["color"] == color_choise:
                if i["round"] == True:
                    teller_rond+=1
                else:
                    teller_niet_rond+=1
        break

if teller_rond > teller_niet_rond:
    verschil = teller_rond- teller_niet_rond
    print(f"Er zijn {verschil} meer ronde vruchten dan niet ronde vruchten in de kleur: {color_choise}")
elif teller_niet_rond > teller_rond:
    verschil = teller_niet_rond - teller_rond
    print(f"Er zijn {verschil} minder ronde vruchten dan niet ronde vruchten in de kleur: {color_choise}")
else:
    print(f"Er zijn {teller_rond} ronde vruchten en {teller_niet_rond} niet ronde vruchten in de kleur: {color_choise}")
