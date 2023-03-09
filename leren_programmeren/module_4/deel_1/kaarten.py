import random
kleuren = ["ruiten", "schoppen", "harten", "klaveren"]
namen = ["2","3","4","5","6","7","8","9","10","boer","vrouw","heer","aas"]
deck = []

for kleur in kleuren:
    for naam in namen:
        deck.append(f"{kleur} {naam}")

for i in range(2):
    deck.append("joker")

for c in range(1,8):
    keuze = random.choice(deck)
    print(f"kaart {c}: {keuze}")
    deck.remove(keuze)
print("")
print(f"deck 47 kaarten {deck}")