door = 1

keuze_1 = input("welkom voor welk werk wilt u soliciteren? dieren dressuur/jongleren/acrobatiek d/j/a ")
if keuze_1 == ("d"):
    dkeuze_1 = int(input("hoelang heeft u al ervaring met dit werk in jaren? "))
    if dkeuze_1 < 4:
        door = door + 1
elif keuze_1 == ("j"):
    jkeuze_1 = int(input("hoelang heeft u al ervaring met dit werk? "))
    if jkeuze_1 < 5:
        door = door + 1
else:
    akeuze_1 = int(input("hoelang heeft u al ervaring met dit werk? "))
    if akeuze_1 < 3:
        door = door + 1

keuze_2 = input("bent u in het bezit van een mbo-4 diploma ondernemen? y/n ")
if keuze_2 ==("n"):
    door = door + 1
keuze_3 = input("bent u in het bezit van een geldig vrachtwagen rijbewijs? y/n")
if keuze_3 == ("n"):
    door = door + 1
else:
    print("bent u in het bezit van een hoge hoed zo nee koop er een!")
    keuze_4 = input("bent u een man of een vrouw m/f")
    if keuze_4 == ("m"):
        mkeuze_1 = int(input("hoeveel cm is uw snor? "))
        if mkeuze_1 < 10:
            door = door + 1
    fkeuze_1 = int(input("hoe lang is uw krulhaar in cm? "))
    if fkeuze_1 < 20:
        door = door + 1
keuze_5 = int(input("wat is uw lengte in cm? "))
if keuze_5 < 150:
    door = door + 1
keuze_6 = int(input("hoeveel kg weegt u? "))
if keuze_6 < 90:
    door = door + 1
keuze_7 = input ("heeft u het certificaat overleven met gevaarlijk personeel? y/n")
if keuze_7 == ("y"):                   
    if door == 1:
        print ("gefeliciteerd u hebt de baan")
    else:
        print ("sorry u mag niet door")