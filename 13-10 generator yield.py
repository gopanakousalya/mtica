def squares(x=0):
    while x < 10:
        x = x + 1
        yield x*x
yieldList=[i for i in squares()]
print(yieldList)

##materialise list from generator using list()
yieldList = list(squares())
print(yieldList)
