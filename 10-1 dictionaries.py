dict={'name':'zara','age':7,'class':'first'}
print(dict)
{'name': 'zara', 'age': 7, 'class': 'first'}
print(dict['class'])
first
dict['age']=8
print(dict)
{'name': 'zara', 'age': 8, 'class': 'first'}
dict['course']='mca'
print(dict)
{'name': 'zara', 'age': 8, 'class': 'first', 'course': 'mca'}
del dict['class']
print(dict)
{'name': 'zara', 'age': 8, 'course': 'mca'}
print(dict)
{}
print
<built-in function print>
print(dict)
{}
dict={'name':'zara','age':7,'class':'first'}
print(dict)
{'name': 'zara', 'age': 7, 'class': 'first'}
dict={'name':'zara','age':7,'class':'first'}
dict.key
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    dict.key
AttributeError: 'dict' object has no attribute 'key'. Did you mean: 'keys'?
dict.keys()
dict_keys(['name', 'age', 'class'])
dict.values()
dict_values(['zara', 7, 'first'])
dict.items()
dict_items([('name', 'zara'), ('age', 7), ('class', 'first')])

