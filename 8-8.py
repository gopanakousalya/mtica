#create a identical list
a=[11,'pyhton','c',12.6,34,21]
##b=a.copy()
##print(b)


##temp=a[:]
##print(temp)


##c=[]
##for i in a:
##    c.append(i)
##print(c)


##d=[i for i in a]
##print(d)



e=[]
stop=len(a)
start=0
while start<stop:
    e.append(a[start])
    start +=1
print(e)
