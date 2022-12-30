def printSeriesDecreasing(ch,n):
    for i in range(n,0,-1):
        print(ch*i)
    return None


inpCh=input("enter a character:")
inpNum=int(input("enter anumber:"))

print('-'*40)
printSeriesDecreasing(inpCh,inpNum)
