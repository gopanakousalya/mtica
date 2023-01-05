class A:
    def first_method(self):
        print("method of class A ... ")
class B:#(A)
    def Second_method(self):
        print("method of class B ... ")

                      
##class C(B):
##    def Third_method(self):
##        print("method of class C ... ")

        
##class C(A,B):#B,A
##    def Third_method(self):
##        print("method of class C ... ")

        
class C(B,A):#B,A
    def Third_method(self):
        print("method of class C ... ")


if __name__=='__main__':
    ob=C()
    ob.first_method()
    ob.Second_method()
    ob.Third_method()
