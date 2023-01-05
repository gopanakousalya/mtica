def printAdd(a,b):
    return a+b
def printSub(a,b):
    return a-b
def printMult(a,b):
    return a*b
def printDiv(a,b):
    return a/b
def choice():
    print("+:Addition")
    print("-:Substraction")
    print("*:Multiplication")
    print("/:Division")
    print("q:Quit")
    return
ColorSelect={"+":printAdd,"-":printSub,"*":printMult,
             "/":printDiv}

while True:
    selection=input("select an arthmetic operation:")
    if selection=='q' or selection=='Q':break
    if ((selection=='+') or (selection=='-') or
        (selection=='*')or(selection=='/')):
       n1=int(input("enter a first no:"))
       n2=int(input("enter a second no:"))
       z=ColorSelect[selection](n1,n2)
       print(n1,selection,n2,'=',z)
