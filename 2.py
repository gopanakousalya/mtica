Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
list1=20
type(list1)
<class 'int'>
list.append(10)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    list.append(10)
TypeError: descriptor 'append' for 'list' objects doesn't apply to a 'int' object
list1.append(10)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    list1.append(10)
AttributeError: 'int' object has no attribute 'append'
list=[15,10]
type(list)
<class 'list'>
list.append(10)
list1
20
list
[15, 10, 10]
list(clear)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    list(clear)
NameError: name 'clear' is not defined
list.(clear)
SyntaxError: invalid syntax

list.clear()
list
[]
list1=[10,25,'pyhton']
list1.count(10)
1
list1.count(25)
1
list1.count('python')
0
len.list1
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    len.list1
AttributeError: 'builtin_function_or_method' object has no attribute 'list1'
len(list1)
3
list1
[10, 25, 'pyhton']
list2=list1
list2
[10, 25, 'pyhton']
del lst[-1]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    del lst[-1]
NameError: name 'lst' is not defined. Did you mean: 'list'?
del list2[-1]
list2
[10, 25]
list1
[10, 25]
list3=list1.copy()
print(id(list1),id(list3))
2944865813760 2944865813312
list1
[10, 25]
list2
[10, 25]
list3
[10, 25]
lst1
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    lst1
NameError: name 'lst1' is not defined. Did you mean: 'list1'?
lst1
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    lst1
NameError: name 'lst1' is not defined. Did you mean: 'list1'?
list1
[10, 25]
list1[:]
[10, 25]
list1[1:]
[25]
list.append([11,22])
list1
[10, 25]
list[-1]
[11, 22]
list1.append(('c','c++','java','python'))
list1
[10, 25, ('c', 'c++', 'java', 'python')]
list1.append('hello')
list1
[10, 25, ('c', 'c++', 'java', 'python'), 'hello']
help list
SyntaxError: invalid syntax
help.list
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    help.list
AttributeError: '_Helper' object has no attribute 'list'
help.(list)
SyntaxError: invalid syntax
help
Type help() for interactive help, or help(object) for help about object.
del list1[3.5]
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    del list1[3.5]
TypeError: list indices must be integers or slices, not float
]
SyntaxError: unmatched ']'
del lst1[3.5]
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    del lst1[3.5]
NameError: name 'lst1' is not defined. Did you mean: 'list1'?
del list1[3:5]
list1
[10, 25, ('c', 'c++', 'java', 'python')]
list1.extend([11,22])
list1
[10, 25, ('c', 'c++', 'java', 'python'), 11, 22]
list1.extend(('c','c++','java','python'))
list1
[10, 25, ('c', 'c++', 'java', 'python'), 11, 22, 'c', 'c++', 'java', 'python']
list1.index(10)
0
dergaftkki69
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    dergaftkki69
NameError: name 'dergaftkki69' is not defined
