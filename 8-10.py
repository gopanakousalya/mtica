def checkEven(num1):
   # num1=int(input("enter a number:"))
    if num1%2==0:

        #print(num1,'is even')
       # str1=str(num1)+"is even"
       return None
##    return str1
    
def checkOdd(num1):
    #num1=int(input("enter a number:"))
    if num1%2==1:
        #print(num1,'is odd')
         return None

num=int(input("enter a no:"))
x=(checkEven(num))
y=(checkOdd(num))

print("x=",x)
print("y",y)

print(checkEven(num))
print(checkOdd(num))
