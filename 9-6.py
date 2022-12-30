##def printMonth(dn):
##    pass
##for i in range(3):
##    inpNum=int(input())
##    print(printMonth(inpNum))


def MonthName(dn):
    if(dn==1):
           return "January"
    if(dn==2):
           return "February"
    if(dn==3):
           return "March"
    if(dn==4):
           return "April"
    if(dn==5):
           return "May"
    if(dn==6):
           return "June"
    if(dn==7):
           return "July"
    if(dn==8):
           return "August"
    if(dn==9):
           return "September"
    if(dn==10):
           return "October"
    if(dn==11):
           return "November"
        
    elif(dn==12):
          return"December"
    else:
        return"Invalid"
for i in range(5):
    inpNum=int(input())
    print(MonthName(inpNum))


