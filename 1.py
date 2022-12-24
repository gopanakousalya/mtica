Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'hello' "world" 'python'
'helloworldpython'
a='hello' "world" 'pyhton'
a
'helloworldpyhton'
type(a)
<class 'str'>
a='hello',"world",'pyhton'
a
('hello', 'world', 'pyhton')
type(a)
<class 'tuple'>
a=23,7.9,'python',3i
SyntaxError: invalid decimal literal
a=23,7.9,'python',3i+27
SyntaxError: invalid decimal literal
a=23,7.9,'python',3+7j
a
(23, 7.9, 'python', (3+7j))
type(a)
<class 'tuple'>
a=15
b=1.5
c='hello'
a
15
b
1.5
c
'hello'
type(a)
<class 'int'>
type(b)
<class 'float'>
type(c)
<class 'str'>
a=(15)
a
15
type(a)
<class 'int'>
a=15,
a
(15,)
type(a)
<class 'tuple'>
