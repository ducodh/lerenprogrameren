gastheer = input("wie is de gastheer? ")
gasten = 5678
drank = True
chips = True

if gastheer != "corbijn" and gastheer == "duco" or drank and (gastheer or gasten >= 4 and gasten <= 20):
    print("start the party")
else:
    print("no party")