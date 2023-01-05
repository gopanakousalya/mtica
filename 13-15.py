#reading a file with an alternate format
with open(r'D:\python.28\kousi.txt')as fo:
    temp=fo.read()
    print(temp)



fo=open(r'D:\python.28\kousi.txt')
temp=fo.read()
print(temp)
fo.close()
