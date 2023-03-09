from fruitmand import fruitmand

for i in range(7):
    if fruitmand[i].get('name') != 'druif':
        print (fruitmand[i].get("color"))
        
print (fruitmand)