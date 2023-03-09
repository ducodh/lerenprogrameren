grootste = 0
klijnste = 1000
delen3 = ""

for i in range(10,0,-1):
    getal = int(input(f"{i} getal(len) tussen 0 en 1000 aub: "))
    if getal > grootste:
        grootste = getal
    if getal < klijnste:
        klijnste = getal
    if getal % 3 == 0:
        delen3 += (f" {getal}")

print(f"dit is de grootste: {grootste}")
print(f"dit is de klijnste: {klijnste}")
print(f"deze getallen kun je delen door 3: {delen3}")