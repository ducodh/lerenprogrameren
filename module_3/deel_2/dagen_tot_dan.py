dag = int(input("welke dag? ma=1 di=2 wo=3 do=4 vr=5 za=6 zo=7 "))

if dag > 7:
    raise NameError("nummer mag niet hoger dan 7 zijn")

lijst = ["ma","di","wo","do","vr","za","zo"]

print (lijst[:dag])