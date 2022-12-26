'abc'+str(5)
'abc5'
'abc'*str(5)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    'abc'*str(5)
TypeError: can't multiply sequence by non-int of type 'str'
'abc'* str(5)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    'abc'* str(5)
TypeError: can't multiply sequence by non-int of type 'str'
'abc'*5
'abcabcabcabcabc'
'abc'+5
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    'abc'+5
TypeError: can only concatenate str (not "int") to str
'abc'+5.0
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    'abc'+5.0
TypeError: can only concatenate str (not "float") to str
'abc'+float(5.0)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    'abc'+float(5.0)
TypeError: can only concatenate str (not "float") to str
str(3.0)*3
'3.03.03.0'
