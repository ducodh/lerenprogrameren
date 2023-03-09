print ("andwoord met ja/nee")

keuze_1 = input ("is de kaas geel? ")
if keuze_1 == ("ja"):
    keuze_2 = input("zitten er gaten in? ")
    if keuze_2 == ("ja"):
        keuze_3 = input("is de kaas belagelijk duur? ")
        if keuze_3 == ("ja"):
            print ("uw kaas is emmenthaler")
        else:
            print ("uw kaas is leerdammer")
    
    else:
            keuze_4 = input ("is de kaas hard als steen? ")
            if keuze_4 == ("ja"):
                print ("uw kaas is parmigiano reggiano")
            else:
                print ("goudse kaas")
else:
    keuze_5 = input ("heeft de kaas blauwe schimmel? ")
    if keuze_5 == ("ja"):
        keuze_6 = input("heeft de kaas een korst? ")
        if keuze_6 == ("ja"):
            print ("uw kaas is blue de rochbaron")
        else:
            print ("uw kaas is foume d'ambert")
    else:
        keuze_7 = input ("heeft de kaas een korst? ")
        if keuze_7 == ("ja"):
            print ("uw kaas is camembert")
        else:
            print("uw kaas is mozzarella")    