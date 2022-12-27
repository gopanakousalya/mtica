print('{0},{1},{2}'.format('apple','banana','carror','pen'))
apple,banana,carror
print('{0},{1},{0},{0},{2}'.format('apple','banana','carror','pen'))
apple,banana,apple,apple,carror
print('{0},{1},{0},{0},{3},{2}'.format('apple','banana','carror','pen'))
apple,banana,apple,apple,pen,carror
print('{0}{1}{0}{0}{3},{2}'.format('apple','banana','carror','pen'))
applebananaappleapplepen,carror
print('{},{}'.format('apple','banana','carrot'))
apple,banana
print('gangully purchased a kg of {},a dozen of {}and half kg of {}'.format('apple','banana','carrot'))
gangully purchased a kg of apple,a dozen of bananaand half kg of carrot
   print('gangully purchased a kg of {0} and {2},kousi purchased a dozen of {2}and{1},madhavi purchased half kg of {0}and{1}and{2}'.format('apple','banana','carrot'))
   
SyntaxError: unexpected indent
print('gangully purchased a kg of {0} and {2},kousi purchased a dozen of {2}and{1},madhavi purchased half kg of {0}and{1}and{2}'.format('apple','banana','carrot'))
gangully purchased a kg of apple and carrot,kousi purchased a dozen of carrotandbanana,madhavi purchased half kg of appleandbananaandcarrot
print('{2},{1},{0}'.format('apple','ball','cat'))
cat,ball,apple
print('{2},{1},{1},{0}'.format('apple','ball','cat'))
cat,ball,ball,apple
print('{2},{1},{0}'.format(*'abcd'))
c,b,a
x,*y,z='computer'
x
'c'
z
'r'
y
['o', 'm', 'p', 'u', 't', 'e']
*x,y='abcd'
y
'd'

print('coordinates:{latitude},{longitude}'.format(latitude='37.24N',longitude='-115.81W'))
coordinates:37.24N,-115.81W
print('welcome:{name},your college is:{college}'.format(name='kousalya',college='mother theresa institutions of computer applications'))
welcome:kousalya,your college is:mother theresa institutions of computer applica
tions
coord=(3,5)
abc=(2,9)
type(coord)
<class 'tuple'>
type(abc)
<class 'tuple'>
abc(0)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    abc(0)
TypeError: 'tuple' object is not callable
abc[0]
2
print('x:{0[1]}; y:{0[1]};abc:{1[0]},{1[1]}'.format(coord,abc))
x:5; y:5;abc:2,9


