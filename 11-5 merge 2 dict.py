dict1={'Ten':10,'Twenty':20,'Thirty':30}
dict2={'Fourty':40,'Fifty':50}




##dict3={**dict1,**dict2}
##print(dict3)




dict3=dict1.copy()
dict3.update(dict2)
print(dict3)
print(dict3)
