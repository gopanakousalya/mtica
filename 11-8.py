sampleDict={
    "name":"kelly",
    "age":25,
    "salary":80000,
    "city":"palamneru"}
keys=["name","salary"]

newDict={i:sampleDict[i] for i in keys}
print(newDict)
    



newDict={}
for i in keys:
    newDict[i]=sampleDict[i]
print(newDict)


res=dict()
for i in keys:
    res.update({i:sampleDict[i]})
print(res)
