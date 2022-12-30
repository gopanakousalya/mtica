def printDay(dn):
    if(dn==1):
        da= "Sunday"
    elif(dn==2):
         da= "Monday"
    elif(dn==3):
         da= "Tuesday"
    elif(dn==4):
         da= "Wednesday"
    elif(dn==5):
         da= "Thursday"
    elif(dn==6):
         da= "Friday"
    elif(dn==7):
         da= "Saturday"
    return da
         
def printDay1(dn):
    if(dn==1):
        da= "Sunday"
    if(dn==2):
         da= "Monday"
    if(dn==3):
         da= "Tuesday"
    if(dn==4):
         da= "Wednesday"
    if(dn==5):
         da= "Thursday"
    if(dn==6):
         da= "Friday"
    if(dn==7):
         da= "Saturday"
    return da
import time
for i in range(7):
    inpNum=int(input())
    start=time.time()
    print(printDay(inpNum))
    print((time.time()-start)*10000000)
    start=time.time()
    print(printDay1(inpNum))
    print((time.time()-start)*10000000)
