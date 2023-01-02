sampleDict={'x':200,'y':800,'z':1000}
if 200 in sampleDict.values():
    print('200 present in a dict')
    

for k,v in sampleDict.items():
    if v==200:
        print("for",v,"key is",k)
