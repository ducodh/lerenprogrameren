#Duco den Hartog PizzaCalculator

small = 3.99
medium = 6.99
large = 11.99

aant_small = float(input ("hoeveel kleine? "))
aant_medium = float(input ("hoeveel medium? "))
aant_large = float(input ("hoeveel large? "))

print ("")
print ("JOE MAMA'S PIZZA PLACE")
print ("")
print (f"{aant_small} kleine pizza tot: {aant_small*small}")
print (f"{aant_medium} kleine pizza tot: {aant_medium*medium}")
print (f"{aant_large} kleine pizza tot: {aant_large*large}")
print ("")
print ("TOTAAL, ")
print (aant_small * small + aant_medium * medium + aant_large *large)