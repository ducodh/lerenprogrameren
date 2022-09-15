a = input("vul een geheel getal in: ")
b = input("vul nog een geheel getal in: ")


if a > b:
    print ("a is het grootste getal")
    max = a
    min = b
    

elif a < b:
    print ("b is het grootste getal")
    max = b
    min = a
    
else:
    print ("a en b zijn even groot")
    max = a
    min = b

print (f"dit is het maximum {max}")
print (f"dit is het minimum {min}")