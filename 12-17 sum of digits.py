class Number:
    def __init__(self,n):
        self.n=n
    def calculateFactorial(self):
        if self.n==0:
            return 1
        res=1
        for i in range(1,self.n+1):
            res*=i
        return res
    def checkEvenOdd(self):
        if self.n%2==0:
            return "Even"
        else:
            return"odd"
    def sumOfDigits(self):
        if self.n<0:
            self.n=abs(self.n)
        temp=str(self.n)
        t=0
        for i in temp:
            t+=int(i)
        return t
        
inp=int(input())
obj=Number(inp)
print('Factorial of',inp,'is',obj.calculateFactorial())
print(inp,"is",obj.checkEvenOdd())
print(inp,"is",obj.sumOfDigits())
