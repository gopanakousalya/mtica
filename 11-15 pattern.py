def printpattern(ch,n):
##    assert(n>=0),'invalid'
    for i in range(n):#(n,0,-1):
        print(ch*i)
ch=input()
n=int(input())
printpattern(ch,n)
##try:
##    printpattern(ch,n)
##except AssertionError as a:
##    print(a)
##    
