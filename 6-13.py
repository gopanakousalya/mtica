import time
inpno=int(input("enter a no:"))
start=time.time()
for i in range(inpno):
    print("i=",i,"i^2=",i*i)
print("time taken by loop:",
      (time.time()-start)*100000)
