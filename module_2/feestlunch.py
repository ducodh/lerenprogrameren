croissant = 0.39
stokbrood = 2.78
kortingsbon = 0.50

aantal_croissant = float(input("hoeveel croisantjes? "))
aantal_stokbrood = float(input("hoeveel stokbroodjes "))
aantal_kortingsbon = float(input("hoeveel kortingsbonnen "))
totaal = aantal_croissant * croissant + aantal_stokbrood * stokbrood - aantal_kortingsbon * kortingsbon

print (" ")
print ("croisantjes " + str(aantal_croissant * croissant))
print ("stokbroodjes " + str(aantal_stokbrood * stokbrood))
print ("korting " + str(aantal_kortingsbon * kortingsbon))
print (" ")
print ("TOTAAL,")
print (totaal)

print (f"De feestlunch kost je bij de bakker {totaal} euro voor de {aantal_croissant} croissantjes en de {aantal_stokbrood} stokbroden als de {aantal_kortingsbon} kortingsbonnen nog geldig zijn!")