land_1 = input("land 1: ")
land_2 = input("land 2: ")
land_3 = input("land 3: ")
nr=1

lijst = []
land = [0,1,2,2,3,1,3]

for i in range(1,7):
    if i == 3 or i == 4:
        nr = 2
    elif i == 5 or i == 6:
        nr = 3
    doelpunten = int(input(f"wetstrijd {nr} land {land[i]}: "))
    lijst.append(doelpunten)

print("")
print(f"wedstrijd {land_1} - {land_2} eindigde in: {lijst[0]} - {lijst[1]}")
print(f"wedstrijd {land_2} - {land_3} eindigde in: {lijst[2]} - {lijst[3]}")
print(f"wedstrijd {land_1} - {land_3} eindigde in: {lijst[4]} - {lijst[5]}")

punten_1 = 0
punten_2 = 0
punten_3 = 0

if lijst[0] < lijst[1]:
    punten_1 += 3
if lijst[0] > lijst[1]:
    punten_2 += 3
if lijst[2] < lijst[3]:
    punten_2 +=3
if lijst[2] > lijst[3]:
    punten_3 +=3
if lijst[4] < lijst[5]:
    punten_1 +=3
if lijst[4] > lijst[5]:
    punten_3+=3

print(f"{land_1}: punten {punten_1}; doelsaldo: {lijst[0] - lijst[1]}") 
print(f"{land_2}: punten {punten_2}; doelsaldo: {lijst[2] - lijst[3]}")
print(f"{land_3}: punten {punten_3}; doelsaldo: {lijst[4] - lijst[5]}")