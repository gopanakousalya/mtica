fo=open(r"D:\python.28\day10a.txt","a")
for i in range(5):
    inpstr=input("enter string:")
    fo.write(inpstr+'\n')
fo.close()
print("written to file")
