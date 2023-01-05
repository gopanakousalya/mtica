class Employee:
    empCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1
    def displayCount(self):
        print("total employee:",Employee.empCount)
    def displayEmployee(self):
        print("name:",self.name,"salary:",self.salary)
emp1=Employee("mahima",5500)
print("total employee",Employee.empCount)
emp2=Employee("abhinum",54000)
emp1.displayEmployee()
emp2.displayEmployee()
print("total employee {0}".format(Employee.empCount))
emp3=Employee("kousi",55500)
emp3.displayCount()
emp2.displayCount()
emp1.displayCount()
print("total employee {0}".format(Employee.empCount))
