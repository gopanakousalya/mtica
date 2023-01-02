sampleDict={
    "name":"kousi",
    "age":25,
    "salary":9000,
    "city":"america"
    }




keys=["name","salary"]
for i in keys:
    sampleDict.pop(i)
    print(sampleDict)

d=dict()
for i in sampleDict.keys()-keys:
    d[i]=sampleDict[i]
    print(d)




sampleDict={i:sampleDict[i]for i in sampleDict.keys()-keys}
print(sampleDict)





