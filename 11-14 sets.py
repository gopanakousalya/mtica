a=set()
type(a)
##<class 'set'>
b={8}
type(b)
##<class 'set'>
c={'mzl','dhana','madhu','kousi'}
type(c)
##<class 'set'>
d={}
type(d)
##<class 'dict'>
a={1,2,3,4,5,6}
b={4,5,6,7,8}
##a+b
##Traceback (most recent call last):
##  File "<pyshell#14>", line 1, in <module>
##    a+b
##TypeError: unsupported operand type(s) for +: 'set' and 'set'
##a.add(b)
##Traceback (most recent call last):
##  File "<pyshell#15>", line 1, in <module>
##    a.add(b)
##TypeError: unhashable type: 'set'
a.union(b)
##{1, 2, 3, 4, 5, 6, 7, 8}
s='kousalya is very good girl'
a=list(s)
a
##['k', 'o', 'u', 's', 'a', 'l', 'y', 'a', ' ', 'i', 's', ' ', 'v', 'e', 'r', 'y', ' ', 'g', 'o', 'o', 'd', ' ', 'g', 'i', 'r', 'l']
set(a)
##{'a', 'o', 'u', 'g', 'e', 'd', 's', 'k', 'r', 'i', 'v', ' ', 'l', 'y'}
a=[11,10,50,67,10,11,67]
b= list(set(a))
b
##[67, 10, 11, 50]
