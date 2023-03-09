dir ={}
item =""
print("om te stopen type 'stop'")
add = ""
while item != "stop":
    item = input("wat wil je toevoegen? ")
    add = item.lower()
    if add != "stop":
        hoeveel = input("hoeveel wil je er? ")
        dir[item] = hoeveel + "x "

print("")
print("-[ bootschapenlijst ]-")
print("")
for i in dir:
    print(i) 
print("")
print("----------------------")