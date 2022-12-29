dict1={"sedan":1500,"svu":2000,"pickup":2500,}
##dict1={"sedan":1500,"svu":2000,"pickup":2500,"minivan":1600,"van":2400,"semi":13600,"bicycle":7,"motorcycle":110}
##dict1
##{'sedan': 1500, 'svu': 2000, 'pickup': 2500, 'minivan': 1600, 'van': 2400, 'semi': 13600, 'bicycle': 7, 'motorcycle': 110}
##dict1.keys()
##dict_keys(['sedan', 'svu', 'pickup', 'minivan', 'van', 'semi', 'bicycle', 'motorcycle'])
##dict1.values()
##dict_values([1500, 2000, 2500, 1600, 2400, 13600, 7, 110])
##dict1.items()
##dict_items([('sedan', 1500), ('svu', 2000), ('pickup', 2500), ('minivan', 1600), ('van', 2400), ('semi', 13600), ('bicycle', 7), ('motorcycle', 110)])


for i in dict1:
    if dict1[i]<5000:print(i)



for i in dict1:
    if dict1[i]<5000:print(i.upper())

ans=[]
##for i in dict1:
##    if dict1[i]<5000:
##        ans.append(i.upper())
##print(ans)

ans=[i.upper() for i in dict1 if dict1[i]<5000]
print(ans)
