cijfer = int(input("welk cijfer wil je de tafel van weten? "))

keer = 1

for c in range (1,11,1):
    andwoord = cijfer * keer
    print(f"{cijfer} x {keer} = {andwoord}")
    keer += 1