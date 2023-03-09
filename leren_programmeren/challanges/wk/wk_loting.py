import random

landen=["nederland",
"engeland",
"verenigde staten",
"frankrijk",
"belgie",
"qatar",
"duitsland",
"denemarken",
"brazilie",
"kroatie",
"spanje",
"servie",
"zwitserland",
"argentinie",
"iran",
"zuid korea",
"japan",
"saudi arabie",
"ecuador",
"uruguay",
"canada",
"ghana",
"senegal",
"portugal",
"polen",
"maroco",
"tunesie",
"kameroen",
"mexico",
"wales",
"australie",
"costa rica",
]

y = 31
nr = 1

for i in range (8):
    print("")
    print(f"groep {nr}")
    nr += 1
    for x in range(4):
        land = random.randint(0,y)
        print(landen[land])
        landen.pop(land)
        y-=1
