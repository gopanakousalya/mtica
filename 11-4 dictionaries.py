D={'g':2,'o':2,'i':1,'n':1,'t':1}
##for i in sorted(D.items(),key=lambda x:x[1],reverse=True):print(i[0],i[1]))
##SyntaxError: unmatched ')'
for i in sorted(D.items(),key=lambda x:x[1],reverse=True):print(i[0],i[1])

##g 2
##o 2
##i 1
##n 1
##t 1
keys=['Ten','Twenty','Thirty'];values=[10,20,30]
zip(keys,values)
##<zip object at 0x0000016E1ED53E40>
for i,j in zip(keys,values):
    print(i,j)

    
##Ten 10
##Twenty 20
##Thirty 30
d=dict()
for i,j in zip(keys,values):
    d[i]=j
    print(d)

    
##{'Ten': 10}
##{'Ten': 10, 'Twenty': 20}
##{'Ten': 10, 'Twenty': 20, 'Thirty': 30}
