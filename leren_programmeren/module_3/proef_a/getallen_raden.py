import random
getal=random.randint(1,1000)
quess = 0
min = 1
max = 1000
teller = 10
goed=0
ronde = 1
print('je gaat 20 rondes van 10 keer raden spelen. als u wil stoppen type: "0000"')
while ronde < 11:
    print(f"ronde: {ronde}")
    print(f"u mag nog {teller} keer raden deze ronde!")
    quess = int(input(f"raad een getal tussen {min}/{max}: "))
    som = abs(getal - quess)
    if quess == getal:
        print("geraden!")
        getal = random.randint(1,1000)
        goed+=1
        teller=11
        min=1
        max=1000
        print(f"u heeft er {goed} goed")
        ronde+=1
    elif quess > getal:
        max = quess
        print("lager")
    elif quess < getal:
        min = quess
        print ("hoger")
    if som <= 20:
        print("je bent heel warm")
    elif som <= 50:
        print("je bent warm")
    if teller == 1:
        print(f"het getal was {getal}")
        print("er word een nieuw getal gekozen")
        teller = 11
        min=1
        max=1000
        getal = random.randint(1,1000)
        print(f"u heeft er {goed} goed")
        ronde+=1
    if getal == 0000:
        break
    teller -=1
print (f"EINDE\nje had er {goed} goed!")