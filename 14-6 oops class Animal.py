class Animal:
    def __init__(self,name,color):
        self.color=color
        self.name=name
    
class Cat(Animal):
    def mew(self):
        print("Cat meows")
class Dog(Animal):
    def bark(self):
        print("Woof")
if __name__=="__main__":
    print(__name__)
    pet1=Dog("Tommy ","Brown")
    pet2=Cat("lucky ","White")

    pet1.bark()
    pet2.mew()
    print(pet1.name)
    print(pet2.name)
