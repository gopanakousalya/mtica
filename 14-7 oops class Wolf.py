class Wolf:
    def __init__(self,name,color):
        self.color=color
        self.name=name
    def bark(self):
        print("Grr...")
class Dog(Wolf):
    def bark(self):
        print("Woof")
pet1=Dog("Tommy ","Brown")

pet1.bark()
pet2=Wolf("jimmy","grey")
pet2.bark()
Dog("abc","xyz").bark()
 #redefining a method of base calss
#in derived class is overriding.
