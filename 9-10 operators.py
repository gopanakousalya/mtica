                       ##identity operators:


##x1=5
##y1=5
##x2='hello'
##y2='hello'
##x3=[1,2,3]
##y3=[1,2,3]
##print(x1 is not y1)
##print(x2 is y2)
##print(x3 is y3)


##output:

##id(x1)
##140727171924904
##id(x2)
##2348205751600
##id(y1)
##140727171924904
##print(id(x3)),(id(y3))
##2348205746176
##(None, 2348165445376)
##print(id(x2)),(id(y2))
##2348205751600
##(None, 2348205751600)




                         ##membership:
##message='hello world'
##dict1={1:'a',2:'b'}

##print('h' in message)
##True
##print('hello' not in message)
##False
##print(1 in dict1)
##True
##print(a in dict1)
##Traceback (most recent call last):
##  File "<pyshell#12>", line 1, in <module>
##    print(a in dict1)
##NameError: name 'a' is not defined
##


##lst1=[10,20,30,'c','java','pyhton']
##print('java' in lst1)
##print('R' not in lst1)
##print('R' not in lst1)

##True
##True

                          ##logical:

##AND:

##print(True and True)
##print(True and False)
##
####OR:
##
##print(True or False)
##
##
####NOT:
##
##
##print(not True)


##a=5
##b=6
##print(a>2 and (b>=6))



x=10
y=4

print('x=',x,'y=',y,'x&y',x&y)
print('x=',x,'y=',y,'x|y=',x|y)
print('x=',x,'~x=',~x)
print('x=',x,'y=',y,'x^y=',x^y)
print('x=',x,'x<<2',x<<2)




























