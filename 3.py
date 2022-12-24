student=[[28,'kousi',79,87],[55,'madhavi',89,99],[1,'dhana',56,98]]
student.sort()
print(student)
student.sort(key=lambda temp:temp[2])
print(student)
student.sort(key=lambda temp:temp[3])
print(student)
