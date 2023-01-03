class check:
    def __init__(self,number):
        self.num=number
    def isArmstrong(self):
        temp=self.num
        res=0
        while(temp!= 0):
            rem=temp%10
            res+=rem**3
            temp//=10
        if self.num==res:
            print(self.num,"is armstrong")
        else:
            print(self.num,"is not armstrong")
        
if __name__=="__main__":
     num=153
     check_Armstrong=check(num)
     check_Armstrong.isArmstrong()
     num=127
     check_Armstrong=check(num)
     check_Armstrong.isArmstrong()
