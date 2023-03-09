Giraffen = 4
Struisvogels = 2
Zebra = 4

Giraffen_aantal = int(input('hoeveel giraffen ziet u? '))
struisvogels_aantal = int(input('en hoeveel struisvogels ziet u? '))
zebra_aantal = int(input("en hoeveel zebra's ziet u? "))

def poten():
    Giraffen_poten = Giraffen_aantal * Giraffen
    struisvogels_poten = struisvogels_aantal * Struisvogels
    zebra_poten = zebra_aantal * Zebra
    aantal_poten = Giraffen_poten + struisvogels_poten + zebra_poten
    string = (f"er zijn {aantal_poten} poten.")
    return(string)    

print(poten())