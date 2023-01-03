class Student:
    college='MTICA'
    course='MCA'
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def displayStudent(self):
        print('name:',self.name.title(),'\nRollno:'+str(self.rollno))
        print('College:'+self.college+'\nCourse:'+self.course)



lstObj=[]
for i in range(5):
   n=input()
   r=int(input())
   temp='obj'+str(i)
   print(temp)
   temp=Student(n,r)
   print(temp,"created")
   lstObj.append(temp)
for i in lstObj:
    i.displayStudent()
   
   
