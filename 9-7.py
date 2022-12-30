def DayNo(dn):
    if(dn==1):
        return "Sunday"
    if(dn==2):
        return "Monday"
    if(dn==3):
        return "Tuesday"
    if(dn==4):
        return "Wednesday"
    if(dn==5):
        return "Thursday"
    if(dn==6):
        return "Friday"
    if(dn==7):
        return "Saturday"
    
    else:
        return "Sunday"
for i in range(4):
    inpNum=int(input())
    print(DayNo(inpNum))
