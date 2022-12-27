lstEven=[]
lstOdd=[]
while(True):
    inpnum=int(input("enter a value(-1 to end):"))
    if inpnum==-1:
        break
    elif inpnum%2==0:
        lstEven.append(inpnum)
    elif inpnum%2==1:
        lstOdd.append(inpnum)
print("Even:",*lstEven)
print("min:",min(lstEven))
print("max:",max(lstOdd))
print("avg:",round(sum(lstEven)/len(lstEven),1))

print("Odd:",*lstOdd)
print("min:",min(lstOdd))
print("max:",max(lstOdd))
print("avg:",round(sum(lstOdd)/len(lstOdd),1))
