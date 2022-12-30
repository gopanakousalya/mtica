def printSeries(n):
    num=1
    for i in range(1,n+1):
        num=1
        print()
        for j in range(i):
            print(num,end='')
        num+=1
    return None

inpNum=int(input())
printSeries(inpNum)

##7
##
##1
##11
##111
##1111
##11111
##111111
##1111111
