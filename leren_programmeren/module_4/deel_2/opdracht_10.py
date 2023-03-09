from fruitmand import fruitmand

dic = {}
for fruit in (fruitmand):
    dic.update({
        fruit.get("weight"):
        fruit.get("name")
        })
print(sorted(dic.items(), reverse =True))