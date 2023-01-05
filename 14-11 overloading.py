'''
magic methods (dunders)

OVERLOADING:
            dunders are special methods which we have  leading and
            trailing double underscore used for operator OVER LOADING.
'''


class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def __mul__(self,obj):
        temp=self.real+obj.real,self.img+obj.img
        return temp
    def __str__(self):
        return(self.real,self.img)
ob1=Complex(3,5)
ob2=Complex(2,1)
ob3=ob1+ob2
print(ob3)
##print(ob4)
