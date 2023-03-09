ticket = 7.45
vip_vr = 0.074

aantal_tickets = int(input ("hoeveel mensen? "))
aantal_minuten = int(input ("hoelang vr? "))
totaal = ticket * aantal_tickets + vip_vr * aantal_tickets * aantal_minuten

print ("TOTAAL,")
print (totaal)

print (f"Dit geweldige dagje-uit met {aantal_tickets} mensen in de Speelhal met {aantal_minuten} minuten VR kost je maar {totaal} euro")