def add(n1,n2):
    temp=n1+n2
    #global variables:a,b,c,add
    #local variables:n1,n2,temp
    global a,b
    a+=10
    print("output of globals:",globals())
    print("output of locals:",locals())
    return temp
a=int(input())
b=int(input())
c=add(a,b)
print(a,'+',b,'=',c)
    
