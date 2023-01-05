def printJan():
    print ("Jan")
    return
def printFeb():
    print ("Feb")
    return
def printMar():
    print ("Mar")
    return
def printApr():
    print ("Apr")
    return
def printMay():
    print ("May")
    return
def printJun():
    print ("Jun")
    return
def printJul():
    print ("Jul")
    return
def printAug():
    print ("Aug")
    return
def printSep():
    print ("Sep")
    return
def printOct():
    print ("Oct")
    return
def printNov():
    print ("Nov")
    return
def printDec():
    print ("Dec")
    return
def choice():
    print("0:Jan")
    print("1:Feb")
    print("2:Mar")
    print("3:Apr")
    print("4:May")
    print("5:Jun")
    print("6:Jul")
    print("7:Aug")
    print("8:Sep")
    print("9:Oct")
    print("10:Nov")
    print("11:Dec")
    print("12:Quit")
    return
MonthSelect={0:printJan,1:printFeb,2:printMar,3:printApr,
            4:printMay,5:printJun,6:printJul,7:printAug,8:printSep,
             9:printOct,10:printNov,11:printDec}
selection=0
while True:
    if selection==12:break
    choice()
    selection=int(input("select a Month option:"))
    if (selection>=0) and (selection<12):
        MonthSelect[selection]()
