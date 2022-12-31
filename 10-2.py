##def printDetail(name,marks):
##    print("name:",name)
##    print("marks:",marks)
##    return None

##printDetail()
##printDetail('manohar')
##printDetail('manohar',87)
##printDetail(87,'manohar')
##printDetail(marks=87,name='manohar')#keyword argument




def printDetail(name,marks=12,age=28):
    print("name:",name)
    print("marks:",marks)
    print("age",age)
    return None

printDetail('manohar')
printDetail('manohar')
printDetail('manohar',87)
printDetail(87,'manohar')
##printDetail(marks=87,name='manohar')#keyword argument

