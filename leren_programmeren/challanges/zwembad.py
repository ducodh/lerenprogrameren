lengte = int(input("wat is de lengte? "))
breete = int(input("wat is de breete? "))
hoogte = float(input("wat is de hoogte? "))
kms = int(input("hoeveel km is het rijden? "))

tot_grond = lengte * breete * hoogte

m2 = lengte * breete

uitgraven = tot_grond * 25
afvoeren = tot_grond * 32.50

if kms < 50 and tot_grond < 20:
    voorrijkosten = 100 + 1.25 * kms
elif kms > 50 and tot_grond < 20:
    voorrijkosten = 100 + 1.15 * kms
elif kms < 50 and tot_grond > 20:
    voorrijkosten = 250 + 2.15 * kms
elif kms > 50 and tot_grond > 20:
    voorrijkosten = 250 + 2.05 * kms

if tot_grond < 20:   
    beton_tegels = m2 * 250
elif tot_grond > 20:
    beton_tegels = m2 * 200


totaal = afvoeren + uitgraven + voorrijkosten + beton_tegels

print(f"offerte voor een zwembad van {lengte} bij {breete} bij {hoogte} meter (inhoud: {tot_grond} m3)")
print(f"uitgraven:                  eur: {uitgraven}")
print(f"afvoeren grond:             eur: {afvoeren}")
print(f"voorrijkosten:              eur: {voorrijkosten}")
print(f"beton + tegel ({m2} m2)       eur: {beton_tegels}")
print(f"totaal                      eur: {totaal}")