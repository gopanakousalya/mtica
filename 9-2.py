def printSeriesDecreasing(ch,n):
    assert isinstance(Ch,str),'first argument should be string'
    assert isinstance(n,int),'first argument should be integer'
    for i in range(n,0,-1):
        print(Ch*i)
    return None


inpCh=input("enter a character:")
inpNum=int(input("enter anumber:"))

print('-'*40)
try:
    printSeriesDecreasing(inpCh,inpNum)
except AssertionError as ob:
    print(ob)
