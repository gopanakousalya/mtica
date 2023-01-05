'''inp=input()
##apple gua mango
temp=inp.split()
temp
#['apple', 'gua', 'mango']
ans=[len(i) for i in temp]
print(*ans)
#5 3 5

inp=input()
##papaya coconut grapes banana
temp=inp.split()
##temp
####['papaya', 'coconut', 'grapes', 'banana']
ans=[len(i) for i in temp]
print(*ans)
####6 7 6 6'''




def solveProblem(s):
    lst=s.split()
    return [len(i) for i in lst]
inp=input()
print(*solveProblem(inp))



##apple gua mango
##5 3 5
##
##
##papaya coconut grapes banana
##6 7 6 6
##
##
##
##kiwi grapes
##4 6
