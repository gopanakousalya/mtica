class Student:
    college='MTICA'
    course='MCA'
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def displayStudent(self):
        print('name:',self.name.title(),'\nRollno:'+str(self.rollno))
        print('College:'+self.college+'\nCourse:'+self.course)
for i in range(5):
   n=input()
   r=int(input())
   obj=Student(n,r)
   obj.displayStudent()
   
