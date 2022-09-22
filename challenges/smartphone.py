iphone = int(input("hoe duur is de iphone? "))
samsung = int(input("hoe duur is de samsung? "))
duurste = iphone - samsung

if iphone >= samsung:
    duurst = iphone
    goedkoopst = samsung
    duurtelefoon = ("iphone")
    goedkooptelefoon = ("samsung")

if samsung > iphone:
    duurst = samsung
    goedkoopst = iphone
    duurtelefoon = ("samsung")
    goedkooptelefoon = ("iphone")

if duurste <= 50:
    koop = ("iphone")
    nietkoop = ("samsung")
    goedduur = ("duurder")

if duurste > 50:
    koop = ("samsung")
    nietkoop = ("iphone")
    goedduur = ("goedkoper")



print (f"de {duurtelefoon} is het duurst, de telefoon kost: {duurst} Euro")
print (f"de {goedkooptelefoon} is het goedkoopst, de telefoon kost {goedkoopst} Euro")
print (f"het advies is dus de {koop} te kopen. Deze is namelijk {duurste} euro {goedduur} dan de {nietkoop} ")