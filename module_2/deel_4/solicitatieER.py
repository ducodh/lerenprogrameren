snor = 1
haar = 1

vrachtwagen = input("hebt u een vrachtwagen rijbewijs? y/n ")
hoed = input("hebt u een hoge hoed? y/n ")
manvrouw = input("bent u een man of een vrouw? m/f ")
if manvrouw == ("m"):
    snor = int(input("hoe lang is uw snor in cm? "))
if manvrouw == ("f"):
    haar = int(input("hoe lang is uw haar in cm? "))
lengte = int(input("hoe lang bent u in cm? "))

if snor == 0:
    raise NameError("opgerot met je kale smoel!")

if vrachtwagen == ("n"):
    raise NameError("ga je rijbewijs halen man sukkel!")
    
if lengte > 220:
    raise NameError("hoe is het klimaat daar boven?")

if vrachtwagen == ("y") and hoed == ("y") and haar == 20 or snor == 10 and lengte > 150 and lengte < 220:
    print ("gefeliciteerd u bent door")

else:
    print ("sorry u bent niet door")
