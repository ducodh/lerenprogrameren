tuple = ("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag")

print("\nAlle dagen van de week zijn:")
for s in range(7):
    print (tuple[s])

print("\nDe werkdagen van de week zijn:")
for i in range(5):
    print (tuple[i])

print("\nDe weekenddagen zijn:")
for c in range(6,7):
    print (tuple[c])

print("\nAlle dagen van de week in omgekeerde volgorde zijn: ")
for x in range(6,-1,-1):
    print (tuple[x])

print("\nDe werkdagen in omgekeerde volgorde zijn:")
for k in range(4,-1,-1):
    print(tuple[k])

print("\nDe weekenddagen in omgekeerde volgorde zijn")
for l in range(6,4,-1):
    print (tuple[l])