uren = int(input("hoe laat is het in uren? "))
minuten= int(input("hoe laat is het in minuten? "))

daguur = 23 - uren
dagmin = 60 - minuten

print(f"{uren}:{minuten}")
print(f"de dag duurt nog {daguur} uur en {dagmin} minuten ")